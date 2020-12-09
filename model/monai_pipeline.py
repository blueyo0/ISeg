# -*- encoding: utf-8 -*-
'''
@File    :   train.py
@Time    :   2020/12/08 12:08:31
@Author  :   Haoyu Wang 
@Contact :   small_dark@sina.com
@Brief   :   使用monai搭建pytorch通用的P-RNet pipeline
'''

import torch
import numpy as np
import random
import argparse

SEED = 666
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
np.random.seed(SEED)  # Numpy module.
random.seed(SEED)  # Python random module.
torch.manual_seed(SEED)
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True
torch.set_default_tensor_type('torch.FloatTensor')





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="monai pipeline of ISeg")
    parser.add_argument(
        "mode", metavar="mode", default="train", choices=("train", "test_train"), type=str, help="mode of workflow"
    )
    parser.add_argument("--data_folder", default=None, type=str, help="training data folder")
    parser.add_argument("--model_folder", default=None, type=str, help="model folder")
    args = parser.parse_args()
    
