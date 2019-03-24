# Imports
from classifier import *
import pandas as pd

nacion_unida = pd.read_json('nacion_unida.json')

clf = SentimentClassifier()

for index, row in nacion_unida.head().iterrows():
    print(row['text'] + ' ==> %.5f' % clf.predict(row['text']))
