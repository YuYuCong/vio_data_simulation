#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:18:24 2017

@author: hyj
"""
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.set_printoptions(suppress=True)
filepath = os.path.abspath('..') + "/bin"

tx_index = 5

# imu gt data
imu_gt_position = []
imu_gt_quaterntions = []
imu_gt_timestamp = []
imu_gt_position = np.loadtxt(filepath + '/imu_pose.txt',
                             usecols=(tx_index, tx_index + 1, tx_index + 2))

# imu euler integral result
data = np.loadtxt(filepath + '/euler_imu_int_pose.txt')
euler_timestamp = data[:, 0]
euler_position = data[:, [tx_index, tx_index + 1, tx_index + 2]]
euler_quaterntions = data[:, [tx_index + 6, tx_index + 3, tx_index + 4,
                              tx_index + 5]]  # qw,qx,qy,qz

# imu midvalue integral result
data = np.loadtxt(filepath + '/midvalue_imu_int_pose.txt')
midvalue_timestamp = data[:, 0]
midvalue_position = data[:, [tx_index, tx_index + 1, tx_index + 2]]
midvalue_quaterntions = data[:, [tx_index + 6, tx_index + 3, tx_index + 4,
                                 tx_index + 5]]  # qw,qx,qy,qz

# imu_noise euler integral result
data = np.loadtxt(filepath + '/euler_imu_int_pose_noise.txt')
euler_noise_timestamp = data[:, 0]
euler_noise_position = data[:, [tx_index, tx_index + 1, tx_index + 2]]
euler_noise_quaterntions = data[:, [tx_index + 6, tx_index + 3, tx_index + 4,
                                    tx_index + 5]]  # qw,qx,qy,qz

# imu_noise midvalue integral result
data = np.loadtxt(filepath + '/midvalue_imu_int_pose_noise.txt')
midvalue_noise_timestamp = data[:, 0]
midvalue_noise_position = data[:, [tx_index, tx_index + 1, tx_index + 2]]
midvalue_noise_quaterntions = data[:, [tx_index + 6, tx_index + 3, tx_index + 4,
                                       tx_index + 5]]  # qw,qx,qy,qz

### plot 3d
fig = plt.figure()
ax = fig.gca(projection='3d')

# show ground truth
ax.plot(imu_gt_position[:, 0], imu_gt_position[:, 1], imu_gt_position[:, 2],
        label='gt')

# show integral with imu ground truth data
ax.plot(euler_position[:, 0], euler_position[:, 1], euler_position[:, 2],
        label='euler_integral')
ax.plot(midvalue_position[:, 0], midvalue_position[:, 1],
        midvalue_position[:, 2],
        label='midvalue_integral')

# show integral with imu noised data
ax.plot(euler_noise_position[:, 0], euler_noise_position[:, 1],
        euler_noise_position[:, 2], label='euler_integral_noise')
ax.plot(midvalue_noise_position[:, 0], midvalue_noise_position[:, 1],
        midvalue_noise_position[:, 2], label='midvalue_integral_noise')

ax.plot([imu_gt_position[0, 0]], [imu_gt_position[0, 1]],
        [imu_gt_position[0, 2]], 'r.',
        label='start')

ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
