import tweepy

#Authenthication
client = tweepy.Client(
    consumer_key="",
    consumer_secret="",
    access_token="",
    access_token_secret=""
)
# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("#COTW_GATO")
# This method returns a Response object, a named tuple with data includes
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# Each Tweet object has a default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)

# By default, this endpoint/methods returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
# response = client.search_recent_tweets("#COTW_GATO", max_results=100)







