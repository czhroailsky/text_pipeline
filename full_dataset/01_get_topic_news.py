from newsapi import NewsApiClient
import json
import pandas as pd
from datetime import datetime

PATH = './full_dataset/'

if __name__ == '__main__':
	## Load key
	with open(PATH + '/news_api.json') as json_file:  
		data = json.load(json_file)

	# Init
	newsapi = NewsApiClient(api_key=data['news_api_key'])

	# /v2/top-headlines
	query = 'amlo tijuana'
	all_articles = newsapi.get_everything(q=query, from_param='2019-01-011', to=datetime.now().strftime('%Y-%m-%d'), language='es', sort_by='relevancy')

	## News dataframe
	dict_ = {'source': [], 'author': [], 'title': [], 'description': [], 'url': [], 'urlToImage': [], 'publishedAt': [], 'content': []}
	for n in all_articles['articles']:
		dict_['source'].append(n['source']['name'])
		dict_['author'].append(n['author'])
		dict_['title'].append(n['title'])
		dict_['description'].append(n['description'])
		dict_['url'].append(n['url'])
		dict_['urlToImage'].append(n['urlToImage'])
		dict_['publishedAt'].append(n['publishedAt'])
		dict_['content'].append(n['content'])

	df = pd.DataFrame(dict_)

	file_name = '_'.join(query.split(' '))
	df.to_json(PATH + 'news_csv/' +  file_name + '.json', orient='records')

	print(df)