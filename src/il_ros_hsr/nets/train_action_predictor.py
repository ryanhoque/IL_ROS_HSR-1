import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import functional as F

from il_ros_hsr.nets.net import ActPredictorNet
from il_ros_hsr.nets import options as opt
from il_ros_hsr.nets import custom_transforms as CT

import argparse, copy, cv2, os, sys, pickle
import time, datetime
import numpy as np
from os.path import join
from collections import defaultdict

TRAIN_INFO = join(opt.NEW_DATA_SSL,'train/data_train_loader.pkl')
VALID_INFO = join(opt.NEW_DATA_SSL,'valid/data_valid_loader.pkl')
TRAIN_CV = join(opt.NEW_DATA_SSL, 'data_train_loader')

def _deprocess(img):
    """Undo the normalization, multiply by 255, then turn to int type."""
    img = img*opt.STD + opt.MEAN
    img = img*255.0
    img = img.astype(int)
    return img
   

def _save_cfg(config_path):
    """Saves `options.txt` which provides info from the `options.py` file.
    Helps us in case we need to figure out what settings we ran for this.
    To be clear, this is not the `args` but what was in `options.py`.
    """
    avoid = ['BLUE', 'GREEN', 'RED', 'BLACK', 'WHITE']
    with open(config_path, 'w') as f:
        # i.e., the variables in `il_ros_hsr.nets.options`
        cfg_dict = opt.__dict__
        for key in sorted(cfg_dict.keys()):
            if key[0].isupper() and key not in avoid:
                cfg_str = '{}: {}\n'.format(key, cfg_dict[key])
                f.write(cfg_str)


def _save_images(imgs_t, imgs_tp1, labels_pos, labels_ang, out_pos, 
                 out_ang, ang_predict, loss, batch_num, phase='valid'):
    """Debugging the data transforms, labels, net predictions, etc.
 
    OpenCV can't save if you use floats. You need: `img = img.astype(int)`.
    But, we also need the axes channel to be last, i.e. (height,width,channel).
    But PyTorch puts the channels earlier ... (channel,height,width).
    The raw depth images in the pickle files were of shape (480,640,3).
 
    Right now, the un-normalized images and predictions are for the RESIZED AND
    CROPPED images. Getting the 'true' un-normalized ones for the validation set
    can be done, but the training ones will require some knowledge of what we
    used for random cropping.
    """
    if not os.path.exists(opt.VALID_TMPDIR):
        os.makedirs(opt.VALID_TMPDIR)
    B = imgs_t.shape[0]
    imgs_t   = imgs_t.cpu().numpy()
    imgs_tp1 = imgs_tp1.cpu().numpy()

    # Iterate through all (data-augmented) images in minibatch and save.
    for b in range(B):
        img_t    = imgs_t[b,:,:,:]
        img_tp1  = imgs_tp1[b,:,:,:]
        targ_pos = labels_pos[b,:]
        targ_ang = labels_ang[b]
        pred_pos = out_pos[b,:]
        # the argmax, i.e., not the logits (those are in `out_ang`)
        pred_ang = ang_predict[b]

        assert img_t.shape == img_tp1.shape == (3,224,224)
        img_t   = img_t.transpose((1,2,0))
        img_tp1 = img_tp1.transpose((1,2,0))
        h,w,c = img_t.shape
 
        # Undo the normalization, multiply by 255, then turn to integers.
        img_t   = _deprocess(img_t)
        img_tp1 = _deprocess(img_tp1)

        # Similarly, deprocess the (x,y) grasp point. To confirm, if we look at
        # the BGR images, we better see 'targ_pos_int' at the red corner.
        targ_pos_int = int(targ_pos[0]*w), int(targ_pos[1]*h)
        pred_pos_int = int(pred_pos[0]*w), int(pred_pos[1]*h)
 
        # Computing 'raw' L2, well for the (224,224) input image ...
        #L2_pix = np.linalg.norm(targ_pos_ing - pred_pos_int)
        L2_pix = np.linalg.norm(np.array(targ_pos_int) - np.array(pred_pos_int))
	L_ang = abs(targ_ang - pred_ang)
        # Later, I can do additional 'un-processing' to get truly original L2s.
 
        # Overlay prediction vs target.
        # Using `img` gets a weird OpenCV error, I had to add 'contiguous' here.
        img = np.ascontiguousarray(img_t, dtype=np.uint8)
        cv2.circle(img, center=targ_pos_int, radius=2, color=opt.RED,   thickness=-1)
        cv2.circle(img, center=targ_pos_int, radius=3, color=opt.BLACK, thickness=1)
        cv2.circle(img, center=pred_pos_int, radius=2, color=opt.BLUE,  thickness=-1)
        cv2.circle(img, center=pred_pos_int, radius=3, color=opt.GREEN, thickness=1)

        # This is the direction. Don't worry about the length, we can't easily get
        # it in pixel space and we keep length in world-space roughly fixed anyway.
        if targ_ang == 0:
            targ_offset = [50, 0]
        elif targ_ang == 1:
            targ_offset = [0, -50]
        elif targ_ang == 2:
            targ_offset = [-50, 0]
        elif targ_ang == 3:
            targ_offset = [0, 50]
        else:
            raise ValueError(targ_ang)
        if pred_ang == 0:
            pred_offset = [50, 0]
        elif pred_ang == 1:
            pred_offset = [0, -50]
        elif pred_ang == 2:
            pred_offset = [-50, 0]
        elif pred_ang == 3:
            pred_offset = [0, 50]
        else:
            raise ValueError(target_ang)

        # Draw both target direction and predicted direction
        targ_goal = (targ_pos_int[0] + targ_offset[0], targ_pos_int[1] + targ_offset[1])
        pred_goal = (pred_pos_int[0] + pred_offset[0], pred_pos_int[1] + pred_offset[1])
        cv2.arrowedLine(img, targ_pos_int, targ_goal, color=opt.BLUE, thickness=2)
        cv2.arrowedLine(img, pred_pos_int, pred_goal, color=opt.GREEN, thickness=2)

        cv2.putText(img=img, 
                    text="pred pos: {}".format(pred_pos_int),
                    org=(10,15),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                    fontScale=0.5, 
                    color=opt.GREEN,
                    thickness=1)

        # Combine images (t,tp1) together and save.
        hstack = np.concatenate((img, img_tp1), axis=1)
        fname = '{}/{}_{}_{}_{:.0f}_{}.png'.format(opt.VALID_TMPDIR, phase, str(batch_num).zfill(3), str(b).zfill(4), L2_pix, L_ang)
        cv2.imwrite(fname, hstack)


def _log(phase, ep_loss, ep_loss_pos, ep_loss_ang, ep_correct_ang):
    """For logging."""
    print("  ({})".format(phase))
    print("loss total:  {:.4f}".format(ep_loss))
    print("loss_pos:    {:.4f}".format(ep_loss_pos))
    print("loss_ang:    {:.4f}".format(ep_loss_ang))
    print("correct_ang: {:.4f}".format(ep_correct_ang))

def train(pretrained_model, args):
    if args.holdout:
        return _train(pretrained_model, args)
    else:
        folds = []
        for i in range(10):
            folds.append(_train(copy.deepcopy(pretrained_model), args, i))
        # return best weights, every all train, every all valid
        # and print the average loss across folds
        avg_loss = sum([min(f[2]['loss']) for f in folds]) / 10.0
        print("AVERAGE VALIDATION LOSS: {}".format(avg_loss))
        best_predictor = min(folds, key=lambda f: min(f[2]['loss']))[0]
        all_train = [f[1] for f in folds]
        all_valid = [f[2] for f in folds]
        return best_predictor, all_train, all_valid

def _train(pretrained_model, args, val_num=-1):
    if val_num > -1:
        print("Fold #{}".format(val_num))
    # To debug transformation(s), look at `custom_transforms.py`.
    transforms_train = transforms.Compose([
        CT.Rescale((256,256)),
        CT.RandomCrop((224,224)),
        CT.RandomHorizontalFlip(),
        CT.ToTensor(),
        CT.Normalize(opt.MEAN, opt.STD),
    ])
    transforms_valid = transforms.Compose([
        CT.Rescale((256,256)),
        CT.CenterCrop((224,224)),
        CT.ToTensor(),
        CT.Normalize(opt.MEAN, opt.STD),
    ])

    if val_num > -1:
        gdata_t = CT.BedGraspDataset(infodir=TRAIN_CV, transform=transforms_train, cv_idx=val_num)
        gdata_v = CT.BedGraspDataset(infodir=TRAIN_CV, transform=transforms_valid, cv_idx=val_num, valid=True)
    else:
        gdata_t = CT.BedGraspDataset(infodir=TRAIN_INFO, transform=transforms_train)
        gdata_v = CT.BedGraspDataset(infodir=VALID_INFO, transform=transforms_valid)

    dataloaders = {
        'train': DataLoader(gdata_t, batch_size=32, shuffle=True, num_workers=8),
        'valid': DataLoader(gdata_v, batch_size=32, shuffle=False, num_workers=8),
    }
    # Use floats due to dividing by these later, for per-epoch results.
    data_sizes = {'train': float(len(gdata_t)), 'valid': float(len(gdata_v))}

    # ADJUST CUDA DEVICE! Be careful about multi-GPU machines like the Tritons!!
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("\nNow training!! On device: {}".format(device))
    print("data_sizes: {}\n".format(data_sizes))

    # Build policy w/pre-trained stem. Can print it to debug.
    act_predictor = ActPredictorNet(pretrained_model, args)
    act_predictor = act_predictor.to(device)

    # Optimizer and loss functions.
    if args.optim == 'sgd':
        optimizer = optim.SGD(act_predictor.parameters(), lr=args.lrate, momentum=0.9)
    elif args.optim == 'adam':
        optimizer = optim.Adam(act_predictor.parameters(), lr=args.lrate)
    else:
        raise ValueError(args.optim)
    criterion_mse  = nn.MSELoss()
    criterion_cent = nn.CrossEntropyLoss()

    # --------------------------------------------------------------------------
    # FINALLY TRAINING!! Here, track loss and the 'original' loss in raw pixels.
    # Use `all_train` and `all_valid` to record statistics for analysis later.
    # --------------------------------------------------------------------------
    since = time.time()
    best_model_wts = copy.deepcopy(act_predictor.state_dict())
    best_loss = np.float('inf')
    all_train = defaultdict(list)
    all_valid = defaultdict(list)

    for epoch in range(args.num_epochs):
        print('')
        print('-' * 30)
        print('Epoch {}/{}'.format(epoch, args.num_epochs-1))
        print('-' * 30)

        # Each epoch has a training and validation phase.
        for phase in ['train', 'valid']:
            if phase == 'train':
                act_predictor.train()
            else:
                act_predictor.eval()
            # Track statistics over _this_ coming epoch only.
            running = defaultdict(list)

            # Iterate over data and labels (minibatches) for ONE epoch.
            for mb in dataloaders[phase]:
                imgs_t     = (mb['img_t']).to(device)           # (B,3,224,224)
                imgs_tp1   = (mb['img_tp1']).to(device)         # (B,3,224,224)
                labels     = (mb['label']).to(device)           # (B,3)
                labels_pos = labels[:,:2].float()               # (B,2)
                labels_ang = torch.squeeze(labels[:,2:].long()) # (B,), needs squeeze

                # Zero the parameter gradients!
                optimizer.zero_grad()

                # Forward: track gradient history _only_ if training
                with torch.set_grad_enabled(phase == 'train'):
                    out_pos, out_ang = act_predictor(imgs_t, imgs_tp1)

                    # Get classification accuracy from the predicted angle probs
                    _, ang_predict = torch.max(out_ang, dim=1)
                    correct_ang = (ang_predict == labels_ang).sum().item()

                    if args.model_type == 1:
                        # First loss needs (B,2). Second (B,) for class _index_.
                        loss_pos = criterion_mse(out_pos, labels_pos)
                        loss_ang = criterion_cent(out_ang, labels_ang)
                        loss = loss_pos + loss_ang
                    elif args.model_type == 2:
                        raise NotImplementedError()
                    elif args.model_type == 3:
                        raise NotImplementedError()
                    else:
                        raise ValueError(args.model_type)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                # Keep track of stats, mult by batch size since we average earlier
                running['loss'].append(loss.item() * imgs_t.size(0))
                running['loss_pos'].append(loss_pos.item() * imgs_t.size(0))
                running['loss_ang'].append(loss_ang.item() * imgs_t.size(0))
                running['correct_ang'].append(correct_ang)

            # We summed (not averaged) the losses earlier, so divide by full size.
            ep_loss        = np.sum(running['loss']) / data_sizes[phase]
            ep_loss_pos    = np.sum(running['loss_pos']) / data_sizes[phase]
            ep_loss_ang    = np.sum(running['loss_ang']) / data_sizes[phase]
            ep_correct_ang = np.sum(running['correct_ang']) / data_sizes[phase]
            _log(phase, ep_loss, ep_loss_pos, ep_loss_ang, ep_correct_ang)

            if phase == 'train':
                all_train['loss'].append(round(ep_loss,5))
                all_train['loss_pos'].append(round(ep_loss_pos,5))
                all_train['loss_ang'].append(round(ep_loss_ang,5))
            else:
                # Can print outputs and labels here for the last minibatch
                # evaluated from the validation set during this epoch.
                #print(out_pos, out_ang, labels)
                all_valid['loss'].append(round(ep_loss,5))
                all_valid['loss_pos'].append(round(ep_loss_pos,5))
                all_valid['loss_ang'].append(round(ep_loss_ang,5))

            # deep copy the model, use `state_dict()`.
            if phase == 'valid' and ep_loss < best_loss:
                best_loss = ep_loss
                best_model_wts = copy.deepcopy(act_predictor.state_dict())
        print('-' * 30)

    time_elapsed = time.time() - since
    print('\nTrained in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    print('Best validation epoch total loss:  {:4f}'.format(best_loss))
    print('  train:\n{}'.format(all_train['loss']))
    print('  valid:\n{}'.format(all_valid['loss']))

    # Load best model weights, make predictions on validation to confirm
    act_predictor.load_state_dict(best_model_wts)
    act_predictor.eval()
    print("\nVisualizing performance of best model on validation set:")

    batch_num = 0
    for mb in dataloaders['valid']:
        imgs_t     = (mb['img_t']).to(device)
        imgs_tp1   = (mb['img_tp1']).to(device)
        labels     = (mb['label']).to(device)
        labels_pos = labels[:,:2].float()
        labels_ang = torch.squeeze(labels[:,2:].long())

        optimizer.zero_grad()
        with torch.set_grad_enabled(False):
            out_pos, out_ang = act_predictor(imgs_t, imgs_tp1)
            _, ang_predict = torch.max(out_ang, dim=1)
            correct_ang = (ang_predict == labels_ang).sum().item()

            loss_pos = criterion_mse(out_pos, labels_pos)
            loss_ang = criterion_cent(out_ang, labels_ang)
            loss = loss_pos + loss_ang
            print("  {} / {} angle accuracy for this mb".format(correct_ang,
                    imgs_t.size(0)))
	    if val_num >= 0: # we are doing CV, so save images by fold number
                batch_num = val_num
            _save_images(imgs_t, imgs_tp1, labels_pos, labels_ang, out_pos, 
                         out_ang, ang_predict, loss, val_num, phase='valid')
            batch_num += 1

    print("Just finished saving validation images! Look at: {}".format(opt.VALID_TMPDIR))
    return act_predictor, all_train, all_valid


if __name__ == "__main__":
    # --------------------------------------------------------------------------
    pp = argparse.ArgumentParser()
    pp.add_argument('--pretrained_model', type=str, default='resnet18')
    pp.add_argument('--num_epochs', type=int, default=30)
    pp.add_argument('--seed', type=int, default=0)
    pp.add_argument('--holdout', action='store_true', default=False)

    # If changing the optimizer, the learning rate must be adjusted as well.
    # I think ~1e-4 for Adam, ~1e-2 for SGD. Adam generally needs lower LRs.
    pp.add_argument('--optim', type=str, default='adam')
    pp.add_argument('--lrate', type=float, default=0.0001)

    # Rely on several options for the loss type. See network class for details.
    pp.add_argument('--model_type', type=int, default=1)
    args = pp.parse_args() 
    # --------------------------------------------------------------------------

    # Bells and whistles, saving stuff, etc.
    torch.manual_seed(args.seed)
    save_dir = opt.get_save_dir(args)
    print("Saving in: {}".format(save_dir))
    _save_cfg(join(save_dir, 'options.txt'))

    # Get pre-trained model and train!
    resnet = opt.get_pretrained_model(args)
    act_predictor, stats_train, stats_valid = train(resnet, args)

    # https://pytorch.org/tutorials/beginner/saving_loading_models.html
    torch.save(act_predictor.state_dict(), join(save_dir,'act_predictor.pt'))
    with open(join(save_dir,'stats_train.pkl'), 'w') as fh:
        pickle.dump(stats_train, fh)
    with open(join(save_dir,'stats_valid.pkl'), 'w') as fh:
        pickle.dump(stats_valid, fh)
    print("\nDone! Look at this directory for results:\n{}".format(save_dir))
