import tweepy
import sys

#Enter Twitter API Key information
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
      file = open('deadpool2_world.txt','a')
      if 'deadpool2' in status.text.lower():
      #if status.coordinates is not None or status.geo is not None or status.place is not None:
        print(status.text)
        print(status.created_at)
        print(status.coordinates)
        print(status.geo)
        print(status.place)
        file.write(str(status.text) + '|--|')
        file.write(str(status.created_at) + '|--|')
        file.write(str(status.geo) + '|--|')
        file.write(str(status.place) + '|--|')
        file.write(str(status.coordinates) + '\n')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#myStream.filter(track=['deadpool2'])
myStream.filter(locations=[-180,-90,180,90])
