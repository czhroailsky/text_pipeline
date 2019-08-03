# Imports
import pandas as pd 
import numpy as np
import statistics

import string
from num2words import num2words
from nltk.corpus import stopwords
import metrics_functions as mf

import plotly.offline as py
import plotly.graph_objs as go

if __name__ == '__main__':
    
    #data = pd.read_json('/Users/jesusreyes/Google Drive/fake_news_resources/raw_data/nacion_unida.json')
    data = pd.read_csv('/Users/jesusreyes/Google Drive/fake_news_resources/raw_data/heraldo_test.csv')
    print(data.info())

    ## Readability metrics

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

        readability.append([index, FS_index, FH_read, GP_com, MM_read, CA_sch])


    readability = pd.DataFrame(readability, columns=['id', 'FS_index', 'FH_read', 'GP_com', 'MM_read', 'CA_sch'])
    readability.set_index('id', inplace=True)
    
    data = pd.concat([data, readability], axis=1)
    data['source'] = 'heraldo'

    print(data['source'].value_counts())

    print('\nFS_index')
    print(data['FS_index'].max())
    print(data['FS_index'].min())

    print('\nFH_read')
    print(data['FH_read'].max())
    print(data['FH_read'].min())

    print('\nGP_com')
    print(data['GP_com'].max())
    print(data['GP_com'].min())

    print('\nMM_read')
    print(data['MM_read'].max())
    print(data['MM_read'].min())

    print('\nCA_sch')
    print(data['CA_sch'].max())
    print(data['CA_sch'].min())

    data.to_csv('./full_dataset/news_csv/heraldo_readability.csv', index=False)