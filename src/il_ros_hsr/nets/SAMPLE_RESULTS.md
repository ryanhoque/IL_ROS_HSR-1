# Tentative Results

On commit 10f24d8034379d4c0a977ab881db5f53baceb913 with ssldata2, here is a
sample output, from running:

```
(py2-torch) seita@hermes1:~/IL_ROS_HSR/src/il_ros_hsr/nets$ python train_action_predictor.py  --holdout
```

I get:

```
Saving in: /nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-17-12-22_000

Now training!! On device: cuda:0
data_sizes: {'train': 159.0, 'valid': 40.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5441
loss_pos:    0.1752
loss_ang:    1.3689
correct_ang: 0.3145
  (valid)
loss total:  1.4220
loss_pos:    0.0586
loss_ang:    1.3633
correct_ang: 0.2750
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3369
loss_pos:    0.0506
loss_ang:    1.2864
correct_ang: 0.4088
  (valid)
loss total:  1.4075
loss_pos:    0.1182
loss_ang:    1.2893
correct_ang: 0.4000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2157
loss_pos:    0.0284
loss_ang:    1.1873
correct_ang: 0.4969
  (valid)
loss total:  1.2505
loss_pos:    0.0381
loss_ang:    1.2124
correct_ang: 0.4250
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0968
loss_pos:    0.0244
loss_ang:    1.0723
correct_ang: 0.5597
  (valid)
loss total:  1.1498
loss_pos:    0.0285
loss_ang:    1.1212
correct_ang: 0.5250
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.9324
loss_pos:    0.0190
loss_ang:    0.9134
correct_ang: 0.7296
  (valid)
loss total:  0.9952
loss_pos:    0.0251
loss_ang:    0.9701
correct_ang: 0.7250
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.7830
loss_pos:    0.0157
loss_ang:    0.7673
correct_ang: 0.8050
  (valid)
loss total:  0.8489
loss_pos:    0.0287
loss_ang:    0.8203
correct_ang: 0.7750
------------------------------

------------------------------
Epoch 6/29
------------------------------
  (train)
loss total:  0.6389
loss_pos:    0.0140
loss_ang:    0.6249
correct_ang: 0.8868
  (valid)
loss total:  0.6947
loss_pos:    0.0223
loss_ang:    0.6724
correct_ang: 0.8750
------------------------------

------------------------------
Epoch 7/29
------------------------------
  (train)
loss total:  0.5090
loss_pos:    0.0124
loss_ang:    0.4966
correct_ang: 0.9245
  (valid)
loss total:  0.5268
loss_pos:    0.0109
loss_ang:    0.5159
correct_ang: 0.9250
------------------------------

------------------------------
Epoch 8/29
------------------------------
  (train)
loss total:  0.3432
loss_pos:    0.0117
loss_ang:    0.3315
correct_ang: 0.9748
  (valid)
loss total:  0.4535
loss_pos:    0.0094
loss_ang:    0.4440
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 9/29
------------------------------
  (train)
loss total:  0.2738
loss_pos:    0.0092
loss_ang:    0.2646
correct_ang: 0.9623
  (valid)
loss total:  0.3735
loss_pos:    0.0120
loss_ang:    0.3615
correct_ang: 0.9000
------------------------------

------------------------------
Epoch 10/29
------------------------------
  (train)
loss total:  0.1793
loss_pos:    0.0084
loss_ang:    0.1709
correct_ang: 0.9874
  (valid)
loss total:  0.2826
loss_pos:    0.0137
loss_ang:    0.2688
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 11/29
------------------------------
  (train)
loss total:  0.1667
loss_pos:    0.0089
loss_ang:    0.1578
correct_ang: 0.9811
  (valid)
loss total:  0.2030
loss_pos:    0.0082
loss_ang:    0.1947
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 12/29
------------------------------
  (train)
loss total:  0.0944
loss_pos:    0.0066
loss_ang:    0.0878
correct_ang: 1.0000
  (valid)
loss total:  0.2039
loss_pos:    0.0067
loss_ang:    0.1972
correct_ang: 0.9250
------------------------------

------------------------------
Epoch 13/29
------------------------------
  (train)
loss total:  0.0744
loss_pos:    0.0083
loss_ang:    0.0661
correct_ang: 0.9874
  (valid)
loss total:  0.1911
loss_pos:    0.0095
loss_ang:    0.1817
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 14/29
------------------------------
  (train)
loss total:  0.0570
loss_pos:    0.0052
loss_ang:    0.0518
correct_ang: 0.9937
  (valid)
loss total:  0.1989
loss_pos:    0.0131
loss_ang:    0.1858
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 15/29
------------------------------
  (train)
loss total:  0.0366
loss_pos:    0.0052
loss_ang:    0.0314
correct_ang: 0.9937
  (valid)
loss total:  0.1871
loss_pos:    0.0104
loss_ang:    0.1768
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 16/29
------------------------------
  (train)
loss total:  0.0337
loss_pos:    0.0067
loss_ang:    0.0270
correct_ang: 1.0000
  (valid)
loss total:  0.1728
loss_pos:    0.0073
loss_ang:    0.1655
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 17/29
------------------------------
  (train)
loss total:  0.0416
loss_pos:    0.0050
loss_ang:    0.0366
correct_ang: 1.0000
  (valid)
loss total:  0.1430
loss_pos:    0.0082
loss_ang:    0.1349
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 18/29
------------------------------
  (train)
loss total:  0.0233
loss_pos:    0.0062
loss_ang:    0.0171
correct_ang: 1.0000
  (valid)
loss total:  0.1141
loss_pos:    0.0052
loss_ang:    0.1089
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 19/29
------------------------------
  (train)
loss total:  0.0146
loss_pos:    0.0046
loss_ang:    0.0100
correct_ang: 1.0000
  (valid)
loss total:  0.1043
loss_pos:    0.0064
loss_ang:    0.0980
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 20/29
------------------------------
  (train)
loss total:  0.0182
loss_pos:    0.0051
loss_ang:    0.0131
correct_ang: 1.0000
  (valid)
loss total:  0.0963
loss_pos:    0.0079
loss_ang:    0.0884
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 21/29
------------------------------
  (train)
loss total:  0.0143
loss_pos:    0.0047
loss_ang:    0.0096
correct_ang: 1.0000
  (valid)
loss total:  0.0941
loss_pos:    0.0047
loss_ang:    0.0894
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 22/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0035
loss_ang:    0.0075
correct_ang: 1.0000
  (valid)
loss total:  0.0938
loss_pos:    0.0058
loss_ang:    0.0880
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 23/29
------------------------------
  (train)
loss total:  0.0093
loss_pos:    0.0030
loss_ang:    0.0063
correct_ang: 1.0000
  (valid)
loss total:  0.0925
loss_pos:    0.0052
loss_ang:    0.0873
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 24/29
------------------------------
  (train)
loss total:  0.0095
loss_pos:    0.0033
loss_ang:    0.0061
correct_ang: 1.0000
  (valid)
loss total:  0.0967
loss_pos:    0.0054
loss_ang:    0.0913
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 25/29
------------------------------
  (train)
loss total:  0.0110
loss_pos:    0.0032
loss_ang:    0.0079
correct_ang: 1.0000
  (valid)
loss total:  0.0937
loss_pos:    0.0047
loss_ang:    0.0889
correct_ang: 0.9750
------------------------------

------------------------------
Epoch 26/29
------------------------------
  (train)
loss total:  0.0157
loss_pos:    0.0041
loss_ang:    0.0117
correct_ang: 0.9937
  (valid)
loss total:  0.1220
loss_pos:    0.0050
loss_ang:    0.1170
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0100
loss_pos:    0.0032
loss_ang:    0.0068
correct_ang: 1.0000
  (valid)
loss total:  0.1449
loss_pos:    0.0062
loss_ang:    0.1387
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0090
loss_pos:    0.0035
loss_ang:    0.0055
correct_ang: 1.0000
  (valid)
loss total:  0.1595
loss_pos:    0.0055
loss_ang:    0.1540
correct_ang: 0.9500
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0097
loss_pos:    0.0038
loss_ang:    0.0059
correct_ang: 1.0000
  (valid)
loss total:  0.1486
loss_pos:    0.0054
loss_ang:    0.1433
correct_ang: 0.9500
------------------------------

Trained in 0m 48s
Best validation epoch total loss:  0.092516
  train:
[1.54411, 1.33691, 1.21575, 1.09675, 0.93239, 0.78298, 0.63891, 0.50903, 0.34322, 0.27378, 0.17928, 0.1667, 0.09438, 0.07436, 0.05695, 0.03664, 0.03372, 0.0416, 0.02333, 0.0146, 0.01824, 0.01431, 0.01104, 0.00927, 0.00946, 0.01103, 0.01572, 0.00997, 0.00896, 0.00973]
  valid:
[1.42195, 1.40751, 1.2505, 1.14976, 0.99522, 0.84893, 0.69469, 0.52685, 0.45346, 0.37351, 0.28256, 0.20299, 0.2039, 0.19115, 0.19886, 0.18712, 0.17282, 0.14304, 0.11411, 0.10434, 0.0963, 0.09405, 0.09381, 0.09252, 0.09673, 0.09367, 0.12197, 0.14487, 0.15948, 0.14864]

Visualizing performance of best model on validation set:
  31 / 32 angle accuracy for this mb
  8 / 8 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/

Done! Look at this directory for results:
/nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-17-12-22_000
```

With cross validation (the default option), we get significantly more verbose output (trimmed here for clarity):
```
(py27) ryanhoque@triton3:~/IL_ROS_HSR/src/il_ros_hsr/nets$ python train_action_predictor.py
```

```
Saving in: /nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-18-13-43_000
Fold #0

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.4897
loss_pos:    0.1223
loss_ang:    1.3674
correct_ang: 0.3017
  (valid)
loss total:  1.3546
loss_pos:    0.0376
loss_ang:    1.3170
correct_ang: 0.4000
------------------------------

------------------------------
Epoch 1/29
------------------------------
  (train)
loss total:  1.3503
loss_pos:    0.0583
loss_ang:    1.2921
correct_ang: 0.3408
  (valid)
loss total:  1.2996
loss_pos:    0.0367
loss_ang:    1.2629
correct_ang: 0.4000
------------------------------

------------------------------
Epoch 2/29
------------------------------
  (train)
loss total:  1.2037
loss_pos:    0.0257
loss_ang:    1.1780
correct_ang: 0.5642
  (valid)
loss total:  1.2124
loss_pos:    0.0288
loss_ang:    1.1835
correct_ang: 0.5500
------------------------------

------------------------------
Epoch 3/29
------------------------------
  (train)
loss total:  1.0524
loss_pos:    0.0235
loss_ang:    1.0289
correct_ang: 0.7207
  (valid)
loss total:  1.0672
loss_pos:    0.0090
loss_ang:    1.0583
correct_ang: 0.6000
------------------------------

------------------------------
Epoch 4/29
------------------------------
  (train)
loss total:  0.8416
loss_pos:    0.0166
loss_ang:    0.8250
correct_ang: 0.8492
  (valid)
loss total:  0.9152
loss_pos:    0.0143
loss_ang:    0.9009
correct_ang: 0.7000
------------------------------

------------------------------
Epoch 5/29
------------------------------
  (train)
loss total:  0.6814
loss_pos:    0.0127
loss_ang:    0.6686
correct_ang: 0.8883
  (valid)
loss total:  0.7645
loss_pos:    0.0140
loss_ang:    0.7505
correct_ang: 0.8500
------------------------------

...

------------------------------
Epoch 27/29
------------------------------
  (train)
loss total:  0.0097
loss_pos:    0.0047
loss_ang:    0.0050
correct_ang: 1.0000
  (valid)
loss total:  0.0696
loss_pos:    0.0065
loss_ang:    0.0631
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 28/29
------------------------------
  (train)
loss total:  0.0082
loss_pos:    0.0043
loss_ang:    0.0039
correct_ang: 1.0000
  (valid)
loss total:  0.0581
loss_pos:    0.0054
loss_ang:    0.0527
correct_ang: 1.0000
------------------------------

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0082
loss_pos:    0.0054
loss_ang:    0.0029
correct_ang: 1.0000
  (valid)
loss total:  0.0579
loss_pos:    0.0041
loss_ang:    0.0539
correct_ang: 1.0000
------------------------------

Trained in 0m 51s
Best validation epoch total loss:  0.057932
  train:
[1.48973, 1.35034, 1.2037, 1.05238, 0.84164, 0.68135, 0.50552, 0.35631, 0.26239, 0.16155, 0.11608, 0.08746, 0.06155, 0.04499, 0.03371, 0.02748, 0.02454, 0.02534, 0.01586, 0.02337, 0.01944, 0.01504, 0.0233, 0.01205, 0.01155, 0.01068, 0.01074, 0.00973, 0.00822, 0.00823]
  valid:
[1.35463, 1.29961, 1.21237, 1.06725, 0.91518, 0.76454, 0.61116, 0.48307, 0.3875, 0.28524, 0.22705, 0.21431, 0.19159, 0.2057, 0.15532, 0.12011, 0.12104, 0.11026, 0.1019, 0.12231, 0.10946, 0.10651, 0.09086, 0.10169, 0.11947, 0.11735, 0.0898, 0.06962, 0.05808, 0.05793]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #1

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5021
loss_pos:    0.1378
loss_ang:    1.3643
correct_ang: 0.3408
  (valid)
loss total:  1.3960
loss_pos:    0.1075
loss_ang:    1.2885
correct_ang: 0.5000
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0127
loss_pos:    0.0042
loss_ang:    0.0085
correct_ang: 1.0000
  (valid)
loss total:  0.1182
loss_pos:    0.0040
loss_ang:    0.1142
correct_ang: 0.9500
------------------------------

Trained in 0m 51s
Best validation epoch total loss:  0.099027
  train:
[1.50206, 1.30278, 1.14506, 0.96291, 0.78085, 0.62, 0.45213, 0.29368, 0.21537, 0.13238, 0.11194, 0.06262, 0.05209, 0.04551, 0.04675, 0.05043, 0.06361, 0.02521, 0.03752, 0.02548, 0.02241, 0.02137, 0.01959, 0.01375, 0.01796, 0.01231, 0.00986, 0.01019, 0.00909, 0.01272]
  valid:
[1.39595, 1.22395, 1.02459, 0.84928, 0.67115, 0.5162, 0.41199, 0.32309, 0.23468, 0.24745, 0.22136, 0.17331, 0.16316, 0.16177, 0.13493, 0.09903, 0.1006, 0.14262, 0.13391, 0.13431, 0.11615, 0.11263, 0.1131, 0.13674, 0.13425, 0.1489, 0.17147, 0.161, 0.1475, 0.11816]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #2

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5335
loss_pos:    0.1619
loss_ang:    1.3716
correct_ang: 0.2402
  (valid)
loss total:  1.4073
loss_pos:    0.0564
loss_ang:    1.3509
correct_ang: 0.2500
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0111
loss_pos:    0.0056
loss_ang:    0.0055
correct_ang: 1.0000
  (valid)
loss total:  0.0834
loss_pos:    0.0061
loss_ang:    0.0773
correct_ang: 1.0000
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.055759
  train:
[1.53346, 1.34383, 1.18582, 1.06059, 0.87506, 0.70824, 0.50077, 0.36276, 0.28254, 0.13143, 0.11827, 0.08886, 0.081, 0.05464, 0.0453, 0.02725, 0.03339, 0.0186, 0.02409, 0.02698, 0.01517, 0.03666, 0.01269, 0.0142, 0.01583, 0.0156, 0.00773, 0.01154, 0.01718, 0.01111]
  valid:
[1.40729, 1.3526, 1.27719, 1.1147, 0.92699, 0.77746, 0.61863, 0.50009, 0.47558, 0.41922, 0.29831, 0.21871, 0.18488, 0.17432, 0.16465, 0.13891, 0.1268, 0.1502, 0.15799, 0.13177, 0.08805, 0.12375, 0.14697, 0.12467, 0.06776, 0.05576, 0.06466, 0.05923, 0.06988, 0.08335]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #3

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5201
loss_pos:    0.1311
loss_ang:    1.3891
correct_ang: 0.2793
  (valid)
loss total:  1.4011
loss_pos:    0.0389
loss_ang:    1.3622
correct_ang: 0.2000
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0096
loss_pos:    0.0038
loss_ang:    0.0058
correct_ang: 1.0000
  (valid)
loss total:  0.2061
loss_pos:    0.0065
loss_ang:    0.1995
correct_ang: 0.9000
------------------------------

Trained in 0m 51s
Best validation epoch total loss:  0.171701
  train:
[1.52013, 1.33617, 1.19161, 1.06369, 0.87212, 0.64566, 0.47676, 0.32913, 0.21812, 0.147, 0.10259, 0.05414, 0.0472, 0.03663, 0.02532, 0.03211, 0.02006, 0.02145, 0.01674, 0.01478, 0.01098, 0.01486, 0.01126, 0.01288, 0.01232, 0.01059, 0.01056, 0.01061, 0.00963, 0.00964]
  valid:
[1.40108, 1.31777, 1.18585, 1.02558, 0.84807, 0.67398, 0.51499, 0.43834, 0.38285, 0.26556, 0.2287, 0.32199, 0.3386, 0.3527, 0.35573, 0.34086, 0.28479, 0.22385, 0.19582, 0.1717, 0.19127, 0.24488, 0.2831, 0.35303, 0.30776, 0.28539, 0.30826, 0.21557, 0.19748, 0.20607]

Visualizing performance of best model on validation set:
  18 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #4

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.4803
loss_pos:    0.1164
loss_ang:    1.3639
correct_ang: 0.3073
  (valid)
loss total:  1.3503
loss_pos:    0.0458
loss_ang:    1.3045
correct_ang: 0.3500
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0099
loss_pos:    0.0076
loss_ang:    0.0023
correct_ang: 1.0000
  (valid)
loss total:  0.1473
loss_pos:    0.0038
loss_ang:    0.1435
correct_ang: 0.9500
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.119822
  train:
[1.48034, 1.32753, 1.16719, 1.0351, 0.83846, 0.63863, 0.47729, 0.33018, 0.21931, 0.14144, 0.09209, 0.06135, 0.0531, 0.05015, 0.03389, 0.01875, 0.02048, 0.01711, 0.01861, 0.03245, 0.01297, 0.01424, 0.01021, 0.0136, 0.00843, 0.01196, 0.00738, 0.00813, 0.0117, 0.0099]
  valid:
[1.35026, 1.24165, 1.12507, 0.99047, 0.77645, 0.57983, 0.44365, 0.32432, 0.26673, 0.19841, 0.19591, 0.17741, 0.15765, 0.1874, 0.17237, 0.13726, 0.11982, 0.14646, 0.1889, 0.21525, 0.19801, 0.20265, 0.1541, 0.15637, 0.18899, 0.18466, 0.19252, 0.16885, 0.14813, 0.14731]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #5

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5117
loss_pos:    0.1621
loss_ang:    1.3496
correct_ang: 0.3743
  (valid)
loss total:  1.3955
loss_pos:    0.0612
loss_ang:    1.3344
correct_ang: 0.4500
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0088
loss_pos:    0.0042
loss_ang:    0.0045
correct_ang: 1.0000
  (valid)
loss total:  0.0951
loss_pos:    0.0088
loss_ang:    0.0863
correct_ang: 1.0000
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.068914
  train:
[1.51168, 1.34882, 1.20485, 1.06393, 0.85232, 0.71137, 0.50804, 0.33789, 0.23177, 0.16591, 0.08897, 0.06222, 0.04854, 0.04478, 0.0326, 0.035, 0.02045, 0.02313, 0.02466, 0.03114, 0.02374, 0.02195, 0.01417, 0.03414, 0.01465, 0.01348, 0.01585, 0.01329, 0.00837, 0.00877]
  valid:
[1.39554, 1.3623, 1.21667, 1.05657, 0.88833, 0.70607, 0.52523, 0.40742, 0.34461, 0.28917, 0.24604, 0.18004, 0.13812, 0.11239, 0.12745, 0.11698, 0.11499, 0.0927, 0.11923, 0.12927, 0.1426, 0.11205, 0.11555, 0.09635, 0.09357, 0.08006, 0.06891, 0.07183, 0.08268, 0.09511]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #6

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5284
loss_pos:    0.1514
loss_ang:    1.3770
correct_ang: 0.3240
  (valid)
loss total:  1.3838
loss_pos:    0.0428
loss_ang:    1.3411
correct_ang: 0.3500
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0089
loss_pos:    0.0036
loss_ang:    0.0052
correct_ang: 1.0000
  (valid)
loss total:  0.2277
loss_pos:    0.0048
loss_ang:    0.2229
correct_ang: 0.9000
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.182634
  train:
[1.52839, 1.32568, 1.18896, 1.05916, 0.83714, 0.63496, 0.46745, 0.30792, 0.23385, 0.14858, 0.10554, 0.08621, 0.05197, 0.05085, 0.02714, 0.03365, 0.01991, 0.02432, 0.01618, 0.0142, 0.00959, 0.00938, 0.01464, 0.01114, 0.01112, 0.01362, 0.01266, 0.01543, 0.00754, 0.00887]
  valid:
[1.38385, 1.33749, 1.22994, 1.06455, 0.86109, 0.73396, 0.63861, 0.50459, 0.40287, 0.37751, 0.39419, 0.42115, 0.29941, 0.23189, 0.22636, 0.27009, 0.29312, 0.27823, 0.26963, 0.24885, 0.25919, 0.26625, 0.25642, 0.22498, 0.2152, 0.20816, 0.21101, 0.18263, 0.20853, 0.22771]

Visualizing performance of best model on validation set:
  18 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #7

Now training!! On device: cuda:0
data_sizes: {'train': 180.0, 'valid': 19.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5570
loss_pos:    0.1877
loss_ang:    1.3693
correct_ang: 0.3833
  (valid)
loss total:  1.3586
loss_pos:    0.0403
loss_ang:    1.3183
correct_ang: 0.4211
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0063
loss_pos:    0.0031
loss_ang:    0.0032
correct_ang: 1.0000
  (valid)
loss total:  0.1278
loss_pos:    0.0043
loss_ang:    0.1235
correct_ang: 0.9474
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.113667
  train:
[1.55703, 1.36269, 1.20526, 1.06771, 0.88775, 0.68746, 0.514, 0.3347, 0.23987, 0.13729, 0.10852, 0.05448, 0.04156, 0.0386, 0.02234, 0.02219, 0.02083, 0.01231, 0.01644, 0.01716, 0.01261, 0.00905, 0.01201, 0.0088, 0.00997, 0.00689, 0.00976, 0.00726, 0.00687, 0.00629]
  valid:
[1.35861, 1.24198, 1.13604, 1.01619, 0.85585, 0.64908, 0.4704, 0.35246, 0.25611, 0.22112, 0.22048, 0.17035, 0.1407, 0.14287, 0.16417, 0.14935, 0.16379, 0.15675, 0.15899, 0.11984, 0.11433, 0.12791, 0.15578, 0.15781, 0.14141, 0.12961, 0.12531, 0.11523, 0.11367, 0.12776]

Visualizing performance of best model on validation set:
  18 / 19 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #8

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.5262
loss_pos:    0.1597
loss_ang:    1.3664
correct_ang: 0.3352
  (valid)
loss total:  1.4383
loss_pos:    0.0882
loss_ang:    1.3501
correct_ang: 0.3000
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0124
loss_pos:    0.0047
loss_ang:    0.0077
correct_ang: 1.0000
  (valid)
loss total:  0.1155
loss_pos:    0.0076
loss_ang:    0.1080
correct_ang: 0.9500
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.034470
  train:
[1.52618, 1.33986, 1.20765, 1.06196, 0.87042, 0.66612, 0.51505, 0.33101, 0.2305, 0.16465, 0.08443, 0.08042, 0.04524, 0.04535, 0.03601, 0.02412, 0.02593, 0.01734, 0.01348, 0.01499, 0.01326, 0.01103, 0.02018, 0.01117, 0.01847, 0.00843, 0.01211, 0.01096, 0.01556, 0.0124]
  valid:
[1.43835, 1.38838, 1.20601, 0.99898, 0.77925, 0.57373, 0.42683, 0.26493, 0.23915, 0.16862, 0.09989, 0.0913, 0.09947, 0.10095, 0.13648, 0.11828, 0.08951, 0.091, 0.08615, 0.09446, 0.07276, 0.05194, 0.0537, 0.05154, 0.09271, 0.096, 0.07207, 0.04197, 0.03447, 0.11554]

Visualizing performance of best model on validation set:
  20 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
Fold #9

Now training!! On device: cuda:0
data_sizes: {'train': 179.0, 'valid': 20.0}


------------------------------
Epoch 0/29
------------------------------
  (train)
loss total:  1.4996
loss_pos:    0.1533
loss_ang:    1.3462
correct_ang: 0.3464
  (valid)
loss total:  1.4317
loss_pos:    0.0805
loss_ang:    1.3511
correct_ang: 0.3000
------------------------------

...

------------------------------
Epoch 29/29
------------------------------
  (train)
loss total:  0.0079
loss_pos:    0.0051
loss_ang:    0.0028
correct_ang: 1.0000
  (valid)
loss total:  0.1575
loss_pos:    0.0042
loss_ang:    0.1533
correct_ang: 0.9500
------------------------------

Trained in 0m 52s
Best validation epoch total loss:  0.141036
  train:
[1.49956, 1.34023, 1.21457, 1.08262, 0.89511, 0.69362, 0.50266, 0.32012, 0.1887, 0.14394, 0.09646, 0.05732, 0.05085, 0.04445, 0.036, 0.02491, 0.02126, 0.01989, 0.01625, 0.0189, 0.01197, 0.0133, 0.01557, 0.00893, 0.01575, 0.01126, 0.0125, 0.00858, 0.01102, 0.00787]
  valid:
[1.43166, 1.36785, 1.11217, 0.8826, 0.69039, 0.50651, 0.34908, 0.25442, 0.21665, 0.1768, 0.20874, 0.24349, 0.21956, 0.19795, 0.18391, 0.15453, 0.14359, 0.15393, 0.20634, 0.23177, 0.22388, 0.19415, 0.19105, 0.20128, 0.24235, 0.23122, 0.18808, 0.15911, 0.14104, 0.15751]

Visualizing performance of best model on validation set:
  19 / 20 angle accuracy for this mb
Just finished saving validation images! Look at: tmp_valid_preds/
AVERAGE VALIDATION LOSS: 0.104496

Done! Look at this directory for results:
/nfs/diskstation/seita/bedmake_ssl/resnet18_2018-11-18-13-43_000
```

