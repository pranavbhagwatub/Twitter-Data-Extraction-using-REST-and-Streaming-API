#Code is referenced from https://www.promptcloud.com/blog/scrape-twitter-data-using-python-r
import tweepy
import json
import sys
import jsonpickle
import os

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = "****"
consumer_secret = "****"
access_token = "****"
access_secret = "****"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (not api):
    print ("Authentication failed")
    sys.exit(-1)

searchQuery = '#Oakland riots -RT'  # Search Query
maxTweets = 10000 
tweetsPerQry = 100  # this is the max the API permits
fName = 'SocialUnrest_tweets.json' # Json file where we store the tweets


sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'a') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                 #places = api.geo_search(query="paris", granularity="city")
                 #place_id = places[0].id
                 new_tweets = api.search(q=searchQuery, count=tweetsPerQry) #q="place:%s"
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded tweets, Saved to".format(tweetCount, fName))


