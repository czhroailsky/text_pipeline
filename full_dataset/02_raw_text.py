import pandas as pd 
import json

PATH = './full_dataset/'

title = [

]

text = [

]

if __name__ == '__main__':

	news = 'guardia_nacional.json'
	folder = 'news_csv/'
	file = PATH + folder + news

	data = pd.read_json(file)

	n = 1
	for index, row in data.iterrows():
		print((' ' + str(n) + ' ') * 30)
		print(row['title'])
		print(row['url'])
		n += 1

	"""raw_text = PATH + folder + news.split('.')[0] + '_text.json'  

	dict_ = {'id': [], 'title': [], 'text': []}

	id_ = 0
	for i in range(len(title)):
		dict_['id'].append(id_)
		dict_['title'].append(title[i])
		dict_['text'].append(text[i])

		id_ += 1

	with open(raw_text, 'w') as fp:
		json.dump(dict_, fp)"""

	"""print(data.shape)
	print(len(title))
	print(len(text))"""