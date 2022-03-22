import os 
import sys 
import time 
import numpy as np 
import open3d as o3d
import pyscancontext as sc

curr_dir = os.path.dirname(__file__)
data_dir = os.path.join(curr_dir, "data/kcp")

scm = sc.SCManager()
scm.print_parameters()

# original cloud 
print('')
source_point_cloud_filename = os.path.join(data_dir, '1531883530.449377000.pcd')
source_o3d = o3d.io.read_point_cloud(source_point_cloud_filename)
print(source_o3d)

cloud = np.asarray(source_o3d.points)

ts = time.time()
scd = scm.make_scancontext(cloud)
te = time.time()
print( f" The time cost of Scan Context Descriptor generation for the original cloud: {(te - ts)*1000:.2f} ms" )
    # e.g.,  The time cost of Scan Context Descriptor generation for the original cloud: 11.21 ms


# downsampled cloud (scan context generally works well for downsampled clouds, please see T-RO paepr for the details)
print('')
voxel_size = 0.35
source_down_o3d = source_o3d.voxel_down_sample(voxel_size=voxel_size)
print(source_down_o3d)

down_cloud = np.asarray(source_down_o3d.points)

ts = time.time()
scd = scm.make_scancontext(down_cloud)
te = time.time()
print( f" The time cost of Scan Context Descriptor generation for the downsample cloud: {(te - ts)*1000:.2f} ms" )
    # e.g.,  The time cost of Scan Context Descriptor generation for the downsample cloud: 2.84 ms
