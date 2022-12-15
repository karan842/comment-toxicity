import os
import argparse
import yaml
import pandas as pd
import numpy as np
import re
import string
from itertools import groupby
from get_data import read_params, get_train_data
from data_cleaning import remove_duplicates, clean_text

import nltk
from nltk.corpus import stopwords

## loading the data
def load_data(config_path):
    config = read_params(config_path)
    df = get_train_data(config_path)
    
    # DATA PREPROCESSING/CLEANING
    df['comment_text'] = df['comment_text'].apply(lambda text: remove_duplicates(text))
    df['comment_text'] = df['comment_text'].apply(lambda text: clean_text(text))
    processed_data_path = config["load_data"]["processed_data"]
    df.to_csv(processed_data_path, index=False)   

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_data(config_path=parsed_args.config)
    print("Working")