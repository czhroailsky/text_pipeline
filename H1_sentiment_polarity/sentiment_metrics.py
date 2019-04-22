# Imports
import pandas as pd
from classifier import *
from nltk.corpus import stopwords

if __name__ == '__main__':

	PATH = './get_raw_data/'

	data = pd.read_json(PATH + 'manual_news_01.json')

	print('--------------- Scores with senti_py -----------------')

	sentiment = []

	for index, row in data.iterrows():

		clf = SentimentClassifier()
		text_predicted = clf.predict(row['text'])
		title_predicted = clf.predict(row['title'])

		sentiment.append([row['id'], text_predicted, title_predicted])

	snt_metric = pd.DataFrame(sentiment, columns=['id', 'text_sentiment', 'title_sentiment'])

	data = pd.merge(data, snt_metric, on='id')

	print(data)

	
	print('\n----------------- Lexicon -------------------')

	pos_lexicon = './H1_sentiment_polarity/positive_words_es.txt'

	with open(pos_lexicon) as f:
		content = f.readlines()

	positive = [x.strip() for x in content] 

	neg_lexicon = './H1_sentiment_polarity/negative_words_es.txt'

	with open(neg_lexicon) as f:
		content = f.readlines()

	negative = [x.strip() for x in content]

	## Preprocess text

	data['text_process'] = data['text'].apply(lambda x: x.replace('\n', '').replace('\t', ''))
	data['text_process'] = data['text_process'].apply(lambda x: x.lower())
	data['text_process'] = data['text_process'].apply(lambda x: str(x).split(' '))
	data['text_process'] = data['text_process'].apply(lambda x: [word for word in x if word not in stopwords.words('spanish')])
	data['text_positive'] = data['text_process'].apply(lambda x: [ w for w in x if w in positive ])
	data['text_negative'] = data['text_process'].apply(lambda x: [ w for w in x if w in negative ])

	print(data['text_positive'])
	print(data['text_negative'])