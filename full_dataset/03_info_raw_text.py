import pandas as pd

PATH = './full_dataset/'

if __name__ == '__main__':

	q = 'pemex_fitch'

	folder = 'news_csv/'
	info = pd.read_json(PATH + folder + q + '.json')
	raw = pd.read_json(PATH + folder + q + '_text.json')

	full = pd.concat([info, raw['text']], axis=1)

	full.to_json(PATH + folder + q + '_full.json', orient='records')