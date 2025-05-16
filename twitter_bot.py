import tweepy

bearer_token = "your bearer token here"

consumer_key="your consumer key here"
consumer_secret="your consumer secret here"
access_token="your access token here"
access_token_secret="your access token secret here"

# App Authentication
client = tweepy.Client(bearer_token=bearer_token)

# User Authentication
'''
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)
'''
# Insert the hashtag you want to be searched here
response = client.search_recent_tweets("Your hashtag here")

tweets = response.data








