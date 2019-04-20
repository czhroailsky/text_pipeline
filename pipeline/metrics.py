# Imports
#from classifier import *
import pandas as pd 
import twitter_functions as tw

if __name__ == '__main__':

	data = pd.read_json('./manual_news.json')

	# Sentiment pretrained analysis

	"""snt_metric = []

	for index, row in data.iterrows():

		clf = SentimentClassifier()
		predicted = clf.predict(row['text'])

		snt_metric.append([row['id'], predicted])

	snt_metric = pd.DataFrame(snt_metric, columns=['id', 'snt_predicted'])
	print(snt_metric)"""

	# Twitter network

	creds = tw.load_credentials()

	for index, row in data.iterrows():
		print(row['title'])

		str_search = row['url']
		query = tw.generate_query(str_search)
		query_df = tw.generate_dataframe(creds, query)
		
		str_search = row['title']
		query = tw.generate_query(str_search)
		query_df = pd.concat([query_df, tw.generate_dataframe(creds, query)])

		query_df = query_df.drop_duplicates(subset=['user'])
		print(query_df.info())

		if not query_df.empty:

			user_followers = []
			n = 0
			for index, row in query_df.iterrows():
				if n <= 10: 
					followers = tw.get_followers(creds, row['user'])
					user_followers.append([row['user'], followers])
				else:
					pass

			user_followers = pd.DataFrame(user_followers, columns=['user', 'followers'])
			print(user_followers)

		else:

			print('nothing_to_see')

		"""if not query_df.empty:

			user_followers = []
			for index, row in data.iterrows():
				followers = tw.get_followers(creds, row['user'])
				user_followers.append([row['user'], followers])

			user_followers = pd.DataFrame(user_followers, columns=['user', 'followers'])

			query_df = pd.merge(query_df, user_followers, on='user')

			print('uwu' * 30)
			print(query_df)
			print('uwu' * 30)

		else:

			pass"""