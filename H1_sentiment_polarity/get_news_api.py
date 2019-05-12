from newsapi import NewsApiClient
import json
import pandas as pd

if __name__ == '__main__':
	## Load key
	with open('./H1_sentiment_polarity/news_api.json') as json_file:  
		data = json.load(json_file)

	# Init
	newsapi = NewsApiClient(api_key=data['news_api_key'])

	# /v2/top-headlines
	all_articles = newsapi.get_everything(q='AMLO medicamentos', from_param='2019-05-11', to='2019-04-11', language='es', sort_by='relevancy')

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

	df.to_json('./H1_sentiment_polarity/q_AMLO_medicamentos.json', orient='records')

	print(df)
