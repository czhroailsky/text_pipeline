import pandas as pd 
import json
import os

PATH = './full_dataset/'

if __name__ == '__main__':

	folder = 'news_csv/'

	files = [x for x in os.listdir(PATH + folder) if 'full' in x ]

	aux = pd.DataFrame()
	for f in files:
		with open(PATH + folder + f) as json_file:  
			data = json.load(json_file)

		data = pd.DataFrame.from_records(data)

		if aux.empty:
			aux = data
		else:
			aux = pd.concat([aux, data])

	aux['text'] = aux['text'].apply(lambda x: x.strip() if isinstance(x, str) else x)

	aux.to_json(PATH + folder + 'full_dataset.json', orient='records')