import os 
import time
import numpy as np 
import open3d as o3d
import pyscancontext as sc


curr_dir = os.path.dirname(__file__)
data_dir = os.path.join(curr_dir, "data/kitti_00_partial")

query_cloud_filepath = os.path.join(data_dir, '000000.bin')
positive_cloud_filepath = os.path.join(data_dir, '000001.bin')
negative_cloud_filepath = os.path.join(data_dir, '000040.bin')

scm = sc.SCManager()

def read_bin(bin_path):
    scan = np.fromfile(bin_path, dtype=np.float32)
    scan = scan.reshape((-1, 4))
    ptcloud_xyz = scan[:, :-1]
    return ptcloud_xyz

def bin2scd(filepath, voxel_size=0.5):
    xyz = read_bin(filepath)
    print( f" The poitn cloud {filepath} is loaded." )
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd_down = pcd.voxel_down_sample(voxel_size=voxel_size)
    xyz_down = np.asarray(pcd_down.points)
    scd = scm.make_scancontext(xyz_down)
    return scd 

print('')
query_scd = bin2scd(query_cloud_filepath)
positive_scd = bin2scd(positive_cloud_filepath)
negative_scd = bin2scd(negative_cloud_filepath)

def calc_scd_dist_and_time(scd1, scd2):
    ts = time.time()
    distance, argmin_rot_idx = scm.scd_distance(scd1, scd2)
    te = time.time()
    t_elaps = te - ts
    return distance, t_elaps

print('')
distance_btn_positive_pair, t1 = calc_scd_dist_and_time(query_scd, positive_scd)
distance_btn_negative_pair, t2 = calc_scd_dist_and_time(query_scd, negative_scd)

print( f" The time cost of SCD distance calculation is: {((t1 + t2)/2)*1000:.2f} ms" )
print( f" The SCD distance between the positive pair is: {distance_btn_positive_pair:.3f}" )
print( f" The SCD distance between the negative pair is: {distance_btn_negative_pair:.3f}" )