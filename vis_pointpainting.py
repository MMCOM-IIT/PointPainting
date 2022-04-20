from curses import has_colors
import open3d as o3d
import numpy as np
import argparse
parser = argparse.ArgumentParser(description='arg parser')
parser.add_argument('--pcd_dir', type=str, default=None,required=True)
args = parser.parse_args()
import os 
painted_path = args.pcd_dir
painted_npy = np.load(painted_path)
# print(painted_npy[:,5])
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(painted_npy[:,:3])
pcd.colors = o3d.utility.Vector3dVector(painted_npy[:,5:8])
o3d.io.write_point_cloud("./painted.ply", pcd)
# o3d.visualization.draw_geometries([pcd])