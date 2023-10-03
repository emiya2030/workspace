import os
import numpy as np
import pandas as pd


folder_path ='/media/runshi/865A9DA45A9D9193/LiDARgait/Pointnet_Pointnet2_pytorch/log/classification/pointnet2_int0.25_lr0.0001/input'

for filename in os.listdir(folder_path):
    #去末尾
    
    
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r') as f:
    # 读取文件的一行，去除最后的逗号，并按逗号分割
        data_str = f.readline().rstrip(',\n').split(',')

    # 将字符串列表转换为浮点数数组
    data = np.array(data_str, dtype=float)
    print(file_path)
    reshaped_data = data.reshape(-1, 3)

# 将新形状的数组写入新的 CSV 文件
    np.savetxt(file_path, reshaped_data, delimiter=',', fmt='%e')