# Imports
import pandas as pd 
import numpy as np
import statistics

import string
from num2words import num2words
from nltk.corpus import stopwords
import metrics_functions as mf

from classifier import *

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
	data = data.dropna()

	### Preprocess text

	## Readanility metrics

	readability = []

	for index, row in data.iterrows():

		# Get number of phrases

		num_sentences = len(mf.get_sentences(row['text']))

		# Get number of words

		text = row['text']
		text = text.lower()
		text = text.translate(str.maketrans('', '', string.punctuation))
		text = text.replace('”', '').replace('“', '')
		text = str(text).split(' ')
		text = [word for word in text if word not in stopwords.words('spanish')]
		
		num_words = len(text)

		# Get number of sílabas 

		num_syllables = sum(mf.count_all_syllables(text))

		# Get Flesch-szigriszt index (perspecuidad)

		P = num_words
		S = num_syllables
		F = num_sentences

		FS_index = mf.flesch_szigriszt_index(P, S, F)

		## Get mean syllables per one hundred words

		hun_words = text[:100]
		mean_syllables = sum(mf.count_all_syllables(hun_words)) / len(hun_words)

		## Get sentences per one hundred words

		hun_words = row['text'].split(' ')[:100]
		mean_sentences = len(mf.get_sentences(' '.join(hun_words))) / len(hun_words)
		
		# Get Fernandez-Huerta (lecturabilidad)

		mean_P = mean_syllables
		mean_F = mean_sentences

		FH_read = mf.fernandez_huerda_readability(mean_P, mean_F)

		# Get number of letters

		num_letters = len(list(row['text'].translate(str.maketrans('', '', string.punctuation)).replace(' ', '')))
		
		# Get Gutierrèz de Polini (comprensibilidad)

		L = num_letters
		P = num_words
		F = num_sentences

		GP_com = mf.gutierres_polini_comprehension(L, P, F)

		# Get mean number of letters per word

		let_per_word = [ len(list(x)) for x in text ]
		x_hat = sum(let_per_word) / len(let_per_word)
		
		# Get variance of number of letters per word

		variance = statistics.variance(let_per_word)

		# Get Muñoz-Muñoz (readability)

		n = num_words
		x_hat = x_hat
		variance = variance

		MM_read = mf.munoz_munoz_read(n, x_hat, variance)

		# Get sentences per hundred words

		hun_sentences = mf.get_sentences(' '.join(hun_words))

		# Get syllables per hundred words

		hun_syllables = mf.count_all_syllables(hun_words)

		# Get Crawford's scolarship

		OP = len(hun_sentences)
		SP = sum(hun_syllables)

		CA_sch = mf.crawford_age(OP, SP)

		readability.append([row['id'], FS_index, FH_read, GP_com, MM_read, CA_sch])

	readability = pd.DataFrame(readability, columns=['id', 'FS_index', 'FH_read', 'GP_com', 'MM_read', 'CA_sch'])
	data = pd.merge(data, readability, on='id')


	## Get sentiment metrics

	sentiment = []

	for index, row in data.iterrows():

		## Sentiment sentipy for title and text

		clf = SentimentClassifier()
		text_predicted = clf.predict(row['text'])
		title_predicted = clf.predict(row['title'])

		## Lexicon positive/negative words

		pos_lexicon = './H1_sentiment_polarity/positive_words_es.txt'

		with open(pos_lexicon) as f:
			content = f.readlines()

		positive = [x.strip() for x in content] 

		neg_lexicon = './H1_sentiment_polarity/negative_words_es.txt'

		with open(neg_lexicon) as f:
			content = f.readlines()

		negative = [x.strip() for x in content]

		## Preprocess text

		text_process = row['text'].replace('\n', '').replace('\t', '')
		text_process = text_process.lower()
		text_process = text_process.translate(str.maketrans('', '', string.punctuation))
		text_process = text_process.replace('”', '').replace('“', '')
		text_process = str(text_process).split(' ')
		text_process = [word for word in text_process if word not in stopwords.words('spanish')]

		# Get positive/negative lists

		pos_count = [ w for w in text_process if w in positive ]
		neg_count = [ w for w in text_process if w in negative ]

		# Get positive and negative rate

		pos_rate = len(pos_count) / len(text_process)
		neg_rate = len(neg_count) / len(text_process)

		sentiment.append([row['id'], title_predicted, text_predicted, pos_rate, neg_rate])

	sentiment = pd.DataFrame(sentiment, columns=['id', 'title_predicted', 'text_predicted', 'pos_rate', 'neg_rate'])
	data = pd.merge(data, sentiment, on='id')

	data = data[['id', 'source', 'title_predicted', 'text_predicted', 'pos_rate', 'neg_rate', 'FS_index', 'FH_read', 'GP_com', 'MM_read', 'CA_sch']]

	print('----------------- Results saved: %s ----------------' %(PATH))	

	data.to_csv(PATH + 'read_sent_q_AMLO_medicamentos.csv', index = False)