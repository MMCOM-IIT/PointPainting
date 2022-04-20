import numpy as np
import os

from yaml import parse
np.set_printoptions(threshold=np.inf)
from torch import ge
import open3d as o3d
import argparse

parser = argparse.ArgumentParser(description='arg parser')
parser.add_argument('--pcd_dir', type=str, default=None,required=True)
args = parser.parse_args()

def get_lidar(path):
    return np.fromfile(str(path), dtype=np.float32).reshape(-1, 4)

np_lidar = get_lidar(path=args.pcd_dir)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np_lidar[:,:3])
o3d.io.write_point_cloud("velodyne_pcd.ply", pcd)
o3d.visualization.draw_geometries([pcd])