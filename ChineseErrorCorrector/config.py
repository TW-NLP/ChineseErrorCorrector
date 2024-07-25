import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(PROJECT_DIR, 'pre_model')
DATA_DIR = os.path.join(PROJECT_DIR, 'data')


class LTPPath(object):
    LTP_MODEL_DIR = os.path.join(MODEL_DIR, 'ltp_tiny')
    LTP_DATA_PATH = os.path.join(DATA_DIR, 'dat_data')

