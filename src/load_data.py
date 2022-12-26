import os
import argparse
import yaml
import pandas as pd
import numpy as np
import re
import string
from itertools import groupby
from get_data import read_params, get_train_data, get_test_data
from data_cleaning import text_data_cleaning

import nltk
from nltk.corpus import stopwords

## loading the data
def load_data(config_path):
    config = read_params(config_path)
    train_df = get_train_data(config_path)
    test_df = get_test_data(config_path)
    
    # DATA PREPROCESSING/CLEANING
    try:
        print("\nCleaning the train data")
        train_df['comment_text_clean'] = train_df['comment_text'].apply(lambda text: text_data_cleaning(text))
        print("\nCleaning the test data")
        test_df['comment_text_clean'] = test_df['comment_text'].apply(lambda text: text_data_cleaning(text))
        print("\nData cleaning process completed! Loding the processed data.")
        processed_train_data_path = config["load_data"]["processed_train_data"]
        processed_test_data_path = config["load_data"]["processed_test_data"]
        train_df.to_csv(processed_train_data_path, index=False)
        test_df.to_csv(processed_test_data_path, index=False)
        print("\nProcessed data loaded successfully!")
    except Exception as e:
        print(e)
       

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    load_data(config_path=parsed_args.config)
    print("Stage 1 completed!")