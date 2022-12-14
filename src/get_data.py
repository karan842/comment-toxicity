import os
import argparse
import yaml
import pandas as pd

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_train_data(config_path):
    config = read_params(config_path)
    train_data_path = config["data_source"]["s3_source"]["train_data"]
    train_df = pd.read_csv(train_data_path)
    return train_df

def get_test_data(config_path):
    config = read_params(config_path)
    test_data_path = config["data_source"]["s3_source"]["test_data"]
    test_df = pd.read_csv(test_data_path)
    return test_df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_train_data(config_path=parsed_args.config)
    # print("Everything is working properly!")
    