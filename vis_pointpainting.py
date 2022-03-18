from curses import has_colors
import open3d as o3d
import numpy as np
# np.set_printoptions(threshold=np.inf)
import os 
painted_npy = '000138.npy' #145 154
painted_path = os.path.join(os.getcwd(),'detector/data/kitti/training/painted_lidar/', painted_npy)
painted_npy = np.load(painted_path)
# print(painted_npy[:,5])
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(painted_npy[:,:3])
pcd.colors = o3d.utility.Vector3dVector(painted_npy[:,5:8])
o3d.io.write_point_cloud("./painted.ply", pcd)
# o3d.visualization.draw_geometries([pcd])