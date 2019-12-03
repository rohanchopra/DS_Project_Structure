'''
import modeling.test
from utils.utils import test_logger as tl

tl('test')
'''
import argparse
from modeling.classification_train import train
from scoring.classification_scoring import score
from configparser import ConfigParser
import pandas as pd
import logging
import sys
import os


file = sys.argv[0]
src_path = str(os.path.dirname(file))
project_path = str(os.path.dirname(src_path))

logging.basicConfig(filename=project_path + "/logs/main.log", filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')

parser = argparse.ArgumentParser(description='Next Product to Buy - Mobile')
parser.add_argument('--train', action="store_true", default=False,
                    dest='train',
                    help="Pass this to perform training of the model.")
results = parser.parse_args()

config = ConfigParser()
config.read(project_path + '/config/config.ini')


def train_model():

    mobile_nptb_train = pd.read_csv(project_path + config.get("DATA", "PATH")
                                    + config.get("DATA", "TRAIN_DATA"))
    train(mobile_nptb_train, config)


def score_model():

    mobile_nptb_score = pd.read_csv(project_path + config.get("DATA", "PATH")
                                    + config.get("DATA", "SCORE_DATA"))\
                          .fillna(0)
    score(mobile_nptb_score, config, project_path, logging)


if results.train:
    train_model()
else:
    score_model()
