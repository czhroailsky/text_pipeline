# Imports
from classifier import *
import pandas as pd

data = pd.read_csv('heraldo_test.csv')

clf = SentimentClassifier()

for index, row in data.head().iterrows():
    print(row['text'] + ' ==> %.5f' % clf.predict(row['text']))
