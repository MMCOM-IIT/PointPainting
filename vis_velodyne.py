import numpy as np
import os
np.set_printoptions(threshold=np.inf)
from torch import ge
import open3d as o3d

training_path= os.getcwd()+'/detector/data/kitti/training/'
# training_path= os.getcwd()+'/detector/data/kitti/gt_database/' #ground_truth
def get_lidar(idx):
    lidar_file = training_path + 'velodyne/' + ('%s.bin' % idx)
    # lidar_file = training_path +  '000000_Pedestrian_0.bin'
    return np.fromfile(str(lidar_file), dtype=np.float32).reshape(-1, 4)

np_lidar = get_lidar(idx='000145')

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np_lidar[:,:3])
o3d.io.write_point_cloud("velodyne_pcd.ply", pcd)
o3d.visualization.draw_geometries([pcd])