# Imports
import pandas as pd
#from classifier import *
from nltk.corpus import stopwords
import es_core_news_md as spacy_es_model
import string

if __name__ == '__main__':

	PATH = './get_raw_data/'

	data = pd.read_json(PATH + 'manual_news_01.json')

	print('--------------- Scores with senti-py -----------------')
	"""
	sentiment = []

	for index, row in data.iterrows():

		clf = SentimentClassifier()
		text_predicted = clf.predict(row['text'])
		title_predicted = clf.predict(row['title'])

		sentiment.append([row['id'], text_predicted, title_predicted])

	snt_metric = pd.DataFrame(sentiment, columns=['id', 'text_sentiment', 'title_sentiment'])

	data = pd.merge(data, snt_metric, on='id')

	print(data)
	"""
	
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
	data['text_process'] = data['text_process'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
	data['text_process'] = data['text_process'].apply(lambda x: x.replace('”', '').replace('“', ''))
	data['text_process'] = data['text_process'].apply(lambda x: str(x).split(' '))
	data['text_process'] = data['text_process'].apply(lambda x: [word for word in x if word not in stopwords.words('spanish')])

	## Lexicon words

	data['text_positive'] = data['text_process'].apply(lambda x: [ w for w in x if w in positive ])
	data['text_negative'] = data['text_process'].apply(lambda x: [ w for w in x if w in negative ])

	print(data)

	## POS tagging
	"""
	nlp = spacy_es_model.load(parser=False, entity=False)

	print('\n----- Positive -----')
	for index, row in data.iterrows():
		print(row['title'])
		for w in row['text_positive']:
			print(w)
			w_index = row['text_process'].index(w)
			if w_index > 0:
				print([row['text_process'][w_index - 1] , row['text_process'][w_index], row['text_process'][w_index + 1]])
			else:
				print([row['text_process'][w_index], row['text_process'][w_index + 1]])

	print('\n----- Negative -----')
	for index, row in data.iterrows():
		print(row['title'])
		for w in row['text_negative']:
			print(w)
			w_index = row['text_process'].index(w)
			if w_index > 0:
				print([row['text_process'][w_index - 1] , row['text_process'][w_index], row['text_process'][w_index + 1]])
			else:
				print([row['text_process'][w_index], row['text_process'][w_index + 1]])
	"""
		#doc = nlp(' '.join(row['text_process']))

		#print('\n' + row['title'])

		#for token in doc:
			#if str(token) in row['text_positive']:
				#print(row['text_process'].index(str(token)))
				#print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)