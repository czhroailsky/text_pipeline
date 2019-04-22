# Imports
import pandas as pd
from classifier import *

if __name__ == '__main__':

	PATH = './get_raw_data/'

	data = pd.read_json(PATH + 'manual_news_01.json')

	print('---------------Scores with senti_py-----------------')