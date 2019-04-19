#Imports
from twython import Twython
import json
import pandas as pd
import time
from bs4 import BeautifulSoup
import time

def load_credentials():
    # Load credentials from json file
    with open("twitter_credentials.json", "r") as file:
        creds = json.load(file)
    return(creds)

def generate_query(query):
    # Create our query
    query = {'q': query,
            'result_type': 'mixed',
            'count': 100
            }
    return(query)

def generate_dataframe(creds, query):
    # Instantiate an object
    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

    # Search tweets
    dict_ = {'user': [], 'date_tweet': [], 'text_tweet': [], 'favorite_count': [], 'user_location': [], 'user_followers': [], 'user_following': [], 'date_user_created': [], 'tweet_source': [], 'hashtags': []}
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
        dict_['hashtags'].append([ x['text'] for x in status['entities']['hashtags'] ])

    # Structure data in a pandas DataFrame for easier manipulation
    df = pd.DataFrame(dict_)
    #df.sort_values(by='favorite_count', inplace=True, ascending=False)

    return(df)

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
  # For item i in a range that is a length of l,
  for i in range(0, len(l), n):
    # Create an index range for l of n items:
    yield l[i:i+n]

def get_followers(creds, user):
    # Instantiate an object
    python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

    followers = python_tweets.get_followers_ids(screen_name = user)

    ids = [ str(x) for x in followers['ids']]

    subset = list(chunks(ids, 100))

    screen_names = []

    for c in subset:
        success = False

        while not success:
            try:
                comma_separated_string = ','.join(c)
                output = python_tweets.lookup_user(user_id=comma_separated_string)

                for u in output:
                    screen_names.append(u['screen_name'])

                success = True
                time.sleep(300)

            except:
                print('Waiting rate limit ...')
                time.sleep(300)
                success = False

    return(screen_names)