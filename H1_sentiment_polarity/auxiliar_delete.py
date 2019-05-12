import pandas as pd

data = pd.read_json('./H1_sentiment_polarity/q_AMLO_medicamentos.json')

for index, row in data.iterrows():
	print(row['title'])
	print(row['url'])
	print('uwu' * 30)