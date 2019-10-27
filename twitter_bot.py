import tweepy
import time
import os

# credentials to login to twitter api

consumer_key =
consumer_secret =
access_key =
access_secret =

# login to twitter account api
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tweepy.API(auth)

# iterates over pictures in models folder
os.chdir('doggo')
for image in os.listdir():
    api.update_with_media(image)
    time.sleep(10)