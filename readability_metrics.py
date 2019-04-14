import pandas as pd
import readability

if __name__ == '__main__':

	data = pd.read_json('./manual_news.json')

	print(data)