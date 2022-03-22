import os 
import sys 
import time 
from functools import wraps

import numpy as np 
import open3d as o3d
import pyscancontext as sc
from test_utils import * 

scm = sc.SCManager()

@timeit
def read_bin(bin_path):
    scan = np.fromfile(bin_path, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    ptcloud_xyz = scan[:, :-1]
    return ptcloud_xyz

@timeit
def downsampling(xyz, voxel_size=0.35):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)
    return np.asarray(pcd_down.points)

@timeit
def make_scancontext(xyz):
    return scm.make_scancontext(xyz)

# @timeit
def bin2scd(filepath, voxel_size=0.35):
    xyz = read_bin(filepath)
    
    use_downsampled_cloud = True
    if use_downsampled_cloud:
        xyz = downsampling(xyz, voxel_size)

    return make_scancontext(xyz) 

dataset_dir = '/data/kitti/'
seq_idx = '08'

seq_dir = os.path.join(dataset_dir, seq_idx)
scans_dir = os.path.join(seq_dir, 'velodyne')

scans_names = os.listdir(scans_dir)
scans_paths = [os.path.join(scans_dir, scan_name) for scan_name in scans_names]
scans_paths.sort()
print(f' KITTI dataset sequence\'s point clouds are from: {scans_dir}')

scd_list = []
for ii, scan_path in enumerate(scans_paths):
    print(scan_path, 'processed.')
    scd = bin2scd(scan_path)
    scd_list.append(scd)

scds = np.array(scd_list)
np.save(seq_idx + '_SCDs.npy', scds)