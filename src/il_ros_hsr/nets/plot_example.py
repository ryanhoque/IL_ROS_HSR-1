import argparse, cv2, os, pickle, sys
from os.path import join
from collections import defaultdict
import numpy as np
np.set_printoptions(suppress=True, linewidth=200, precision=4)

from il_ros_hsr.nets import options as opt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')


def plot_loss_curves(stats_t, stats_v):
    """Simple plot to observe performance.
    """
    nrows, ncols = 1, 2
    fig, ax = plt.subplots(nrows, ncols, squeeze=False, figsize=(14*ncols,9*nrows))

    ax[0,0].set_title('Training Loss', fontsize=opt.tsize)
    ax[0,1].set_title('Validation Loss', fontsize=opt.tsize)
    ax[0,0].set_xlabel('Epoch', fontsize=opt.tsize)
    ax[0,1].set_xlabel('Epoch', fontsize=opt.tsize)

    t_matrix = np.vstack([np.array(elem['loss']) for elem in stats_t])
    t_mean = np.mean(t_matrix, axis=0)
    t_std = np.std(t_matrix, axis=0)

    v_matrix = np.vstack([np.array(elem['loss']) for elem in stats_v])
    v_mean = np.mean(v_matrix, axis=0)
    v_std = np.std(v_matrix, axis=0)

    ax[0,0].plot(t_mean)
    ax[0,0].fill_between(np.arange(30), t_mean - t_std, t_mean + t_std, alpha=0.4)
    ax[0,1].plot(v_mean)
    ax[0,1].fill_between(np.arange(30), v_mean - v_std, v_mean + v_std, alpha=0.4)

    # Bells and whistles
    for r in range(nrows):
        for c in range(ncols):
            leg = ax[r,c].legend(loc="best", ncol=2, prop={'size':opt.legendsize})
            for legobj in leg.legendHandles:
                legobj.set_linewidth(5.0)
            ax[r,c].tick_params(axis='x', labelsize=opt.ticksize)
            ax[r,c].tick_params(axis='y', labelsize=opt.ticksize)
    plt.tight_layout()

    # Finally, save.
    figname = join(opt.FIG_TMPDIR, 'plot_loss_curves.png')
    plt.savefig(figname)
    print("\nJust saved: {}".format(figname))

def plot_valid_chart(valid):
    """Bar chart of L2 pixel loss on each (transformed) validation image after training.
    """
    nrows, ncols = 1, 1
    fig, ax = plt.subplots(nrows, ncols, squeeze=False, figsize=(14*ncols,9*nrows))

    ax[0,0].set_title('Prediction Error', fontsize=opt.tsize)
    ax[0,0].set_xlabel('Image', fontsize=opt.tsize)
    ax[0,0].set_ylabel('L2 Pixel Loss', fontsize=opt.tsize)

    ax[0,0].bar(np.arange(len(valid)), valid)

    # Bells and whistles
    for r in range(nrows):
        for c in range(ncols):
            leg = ax[r,c].legend(loc="best", ncol=2, prop={'size':opt.legendsize})
            for legobj in leg.legendHandles:
                legobj.set_linewidth(5.0)
            ax[r,c].tick_params(axis='x', labelsize=opt.ticksize)
            ax[r,c].tick_params(axis='y', labelsize=opt.ticksize)
    plt.tight_layout()

    # Finally, save.
    figname = join(opt.FIG_TMPDIR, 'plot_bars_valid.png')
    plt.savefig(figname)
    print("\nJust saved: {}".format(figname))


if __name__ == "__main__":
    # Perhaps make this more formalized?
    # Could alternatively save in directory corresponding to HEAD?
    if not os.path.exists(opt.FIG_TMPDIR):
        os.makedirs(opt.FIG_TMPDIR)

    pp = argparse.ArgumentParser()
    pp.add_argument('--model', type=str, required=True)
    args = pp.parse_args()

    HEAD  = '/nfs/diskstation/seita/bedmake_ssl'
    train_pth = join(HEAD, args.model, 'stats_train.pkl')
    valid_pth = join(HEAD, args.model, 'stats_valid.pkl')
    
    with open(train_pth, 'r') as fh:
        stats_train = pickle.load(fh)
    with open(valid_pth, 'r') as fh:
        stats_valid = pickle.load(fh)

    valid_losses = sorted([int(filename.split('_')[3]) for filename in os.listdir(opt.VALID_TMPDIR)])
    num_incorrect_angle = 0
    incorrect_angles = []
    for filename in os.listdir(opt.VALID_TMPDIR):
        diff = int(filename.split('_')[-1][:-4]) # number after the last underscore is angle difference
        if diff:
            num_incorrect_angle += 1
            incorrect_angles += [diff]

    plot_loss_curves(stats_train, stats_valid)
    plot_valid_chart(valid_losses)
    print("Number of incorrect angle predictions: {}/{}".format(num_incorrect_angle, len(valid_losses)))
    print("Angle differences: {}".format(incorrect_angles))
