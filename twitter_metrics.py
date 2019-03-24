#Imports
from twython import Twython
import json
import pandas as pd
import time
from bs4 import BeautifulSoup

def load_credentials():
    # Load credentials from json file
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)
    return(creds)

def generate_query(query):
    # Create our query
    query = {'q': query,
            'result_type': 'recent',
            'count': 100
            }
    return(query)

def generate_dataframe(creds, query):
    # Instantiate an object
    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

    # Search tweets
    dict_ = {'user': [], 'date_tweet': [], 'text_tweet': [], 'favorite_count': [], 'user_location': [], 'user_followers': [], 'user_following': [], 'date_user_created': [], 'tweet_source': []}
    for status in python_tweets.search(**query)['statuses']:
        dict_['user'].append(status['user']['screen_name'])
        dict_['date_tweet'].append(time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status['created_at'],'%a %b %d %H:%M:%S +0000 %Y')))
        dict_['text_tweet'].append(status['text'])
        dict_['favorite_count'].append(status['favorite_count'])
        html = status['source']
        soup = BeautifulSoup(html)
        dict_['tweet_source'].append(soup.text)
        dict_['user_location'].append(status['user']['location'])
        dict_['user_followers'].append(status['user']['followers_count'])
        dict_['user_following'].append(status['user']['friends_count'])
        dict_['date_user_created'].append(time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(status['user']['created_at'],'%a %b %d %H:%M:%S +0000 %Y')))

    # Structure data in a pandas DataFrame for easier manipulation
    df = pd.DataFrame(dict_)
    #df.sort_values(by='favorite_count', inplace=True, ascending=False)

    return(df)

if __name__ == "__main__":

    creds = load_credentials()

    # String to search
    str_srch = '#GOT'

    # Generate query
    query = generate_query(str_srch)

    # Generate dataframe
    query_df = generate_dataframe(creds, query)

    print(query_df)
