'''
    Spliting the data into train and validation for model training.
'''

## Importing the libraries
import os
import re
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_data(config_path):
    config = rerad_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    data_path = config["load_data"]["processed_data"]
    split_ratio = config["split_data"]["test_size"]
    random_state = config["base"]["random_state"]
    
    
    