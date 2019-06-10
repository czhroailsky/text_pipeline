# Imports
import pandas as pd 
import numpy as np
import statistics

import string
from num2words import num2words
from nltk.corpus import stopwords
import metrics_functions as mf

from classifier import *

PATH = './full_dataset/'

if __name__ == '__main__':

	folder = 'news_csv/'
	file = 'full_dataset.json'

	data = pd.read_json(PATH + folder + file)
	data = data[data['text'] != '-1']
	data = data[data['text'] != '']
	data = data.dropna(subset=['text'])
	data = data.drop_duplicates()

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

		readability.append([FS_index, FH_read, GP_com, MM_read, CA_sch])

	readability = pd.DataFrame(readability, columns=['FS_index', 'FH_read', 'GP_com', 'MM_read', 'CA_sch'])
	
	print(data.head())
	print(data.info())
	print(readability.head())
	print(readability.info())