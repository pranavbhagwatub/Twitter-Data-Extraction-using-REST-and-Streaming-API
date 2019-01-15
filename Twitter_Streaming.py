import tweepy
import json
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = "****"
consumer_secret = "****"
access_token = "****"
access_secret = "****"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            file = open('Paris_tweets.json', 'a')
            print("Writing data to JSON...")
            file.write(data)

            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True
		


twitter_stream =Stream(auth, MyListener())
##twitter_stream.search(q="Environment", count=5000)

#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(locations=[-74.2591,40.4774,-73.7002,40.9162]) --NYC
#twitter_stream.filter(locations=[77.048515,28.481264,77.241074,28.645683]) --Delhi_tweets
twitter_stream.filter(locations=[2.224122,48.815575,2.46976,48.902157])
#twitter_stream.filter(locations=[-73.935242,40.730610])
#twitter_stream.filter(languages=["en"], track=["military", "police", "injured", "Rioting","Violance"])
#twitter_stream.filter(languages=["en"], track=["military", "police", "injured", "Rioting","Violance"])

#track=["a", "the", "i", "you", "u"] --english
#languages=["es"], track=["a", "tu", "al", "u --spanish
##languages=["hi"], track=["ek", "tu", "tum", "aj","a"] --hindi
#twitter_stream.filter(languages=["fr"], track=["le", "de", "un", "a","et"]) --french
#twitter_stream.filter(languages=["th"], track=["wan-níi", "tham", "dii", "lae4","waa3"]) --thai



#twitter_stream.filter(track=['#Social unrest'])


