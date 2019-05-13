# Imports
import pandas as pd 
import numpy as np

if __name__ == '__main__':

	PATH = './H1_sentiment_polarity/'

	print('----------------- Computing metrics ----------------')

	# Data from news api	
	news = pd.read_json(PATH + 'q_AMLO_medicamentos.json')
	news['id'] = news.index

	# Data from manual text
	mate = pd.read_json(PATH + 'q_AMLO_medicamentos_text.json')
	mate['text'] = mate['text'].apply(lambda x: x.replace('\t', '').replace('\n', ''))
	mate['text'] = mate['text'].apply(lambda x: np.nan if x == 'NaN' else x)

	data = pd.merge(news, mate[['id', 'text']], on='id')

	print(data.head())
	print(data.info())