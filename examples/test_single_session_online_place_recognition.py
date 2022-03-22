import os 
import sys 
import time 
from functools import wraps

import numpy as np 
import open3d as o3d
import pyscancontext as sc

from test_utils import * 

# place recognizer 
scm = sc.SCManager()

# loop parameters 
LOOP_THRES = 0.2

# load pre-made data 
@timeit
def load_data(seq_idx):
    curr_dir = os.path.dirname(__file__)
    data_dir = os.path.join(curr_dir, "data/SCD/KITTI")
    scds = np.load(os.path.join(data_dir, seq_idx, 'SCDs.npy'))
    return scds

seq_idx = '00'
scds = load_data(seq_idx)

@timeit_sec
def run_sequence():
    # sensor data stream 
    num_scds = scds.shape[0]
    for ii in range(num_scds):
        # point cloud to scd 
        #  this was done in batch for the fast demo. see test_batch_scd_saver.py

        # query data
        scd = scds[ii, :]

        # retrieval (querying with online construction of kdtree)
        scm.add_scancontext(scd)
        nn_idx, nn_dist, yaw_diff = scm.detect_loop()
        if nn_idx == -1: # skip the very first scans (see NUM_EXCLUDE_RECENT in Scancontext.h) 
            continue 

        if nn_dist < LOOP_THRES:
            print(f'query: scan {ii}')
            print(f' detected nn node - idx: {nn_idx}, distance: {nn_dist:.3f}, yaw_diff: {np.rad2deg(yaw_diff):.1f} deg')
                # note: if use 60 sectors for a SCD, yaw_diff's minimum resolution is 6 deg.

run_sequence()


# todo 
# '''
#  visualization 
# '''
# # read gt pose to draw the matches 
# poses = np.loadtxt(os.path.join(seq_dir, 'poses.txt'))
# poses_xyz = poses[:, (3,7,11)] # actually cam pose 
# poses_o3d = o3d.geometry.PointCloud()
# poses_o3d.points = o3d.utility.Vector3dVector(poses_xyz)
# o3d.visualization.draw_geometries([poses_o3d])


