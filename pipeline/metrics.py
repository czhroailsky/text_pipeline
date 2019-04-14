# Imports
from classifier import *
import pandas as pd 
import twitter_functions as tw

if __name__ == '__main__':

	data = pd.read_json('./manual_news.json')
	print(data)

	# Sentiment pretrained analysis

	snt_metric = []

	for index, row in data.iterrows():

		clf = SentimentClassifier()
		predicted = clf.predict(row['text'])

		snt_metric.append([row['id'], predicted])

	snt_metric = pd.DataFrame(snt_metric, columns=['id', 'snt_predicted'])
	print(snt_metric)

	# Twitter network

	creds = tw.load_credentials()

	for index, row in data.iterrows():

		str_search = row['url']
		query = tw.generate_query(str_search)
		query_df = tw.generate_dataframe(creds, query)
		
		str_search = row['title']
		query = tw.generate_query(str_search)
		query_df = pd.concat([query_df, tw.generate_dataframe(creds, query)])

		query_df = query_df.drop_duplicates(subset=['user'])

		print(query_df)


