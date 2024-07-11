import pandas as pd
import numpy as np
import argparse 
import yaml
#from pkgutil import get_data


def get_data(config_path):
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_data"]
    df = pd.read_csv(data_path,sep=",", encoding="utf-8")
    #print()
    return df

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)


if __name__ == "__main___":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="parse.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path = parsed_args.config)