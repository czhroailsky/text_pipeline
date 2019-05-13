import pandas as pd

data = pd.read_json('./H1_sentiment_polarity/q_AMLO_medicamentos.json')
data['id'] = data.index

for index, row in data.iterrows():
	print(row['id'])
	print(row['title'])
	print(row['url'])
	print('uwu' * 30)