# module oath
import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="xqIOKUMXfvzvCckqfxIqnMrYk"
consumer_secret="YfjHXWNek98tv4WHXWpaHKJsLQVkXE5KYQDPZyPk8qRbGfIkz8"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token="1193427579035766784-AKi5gMOrDn01mBq8i76qHzNzVKzPsw"
access_token_secret="DqzFO5vCWqgZKDBLdZFi14NtjlXjo6OJJrE1LRaOsDsWP"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def getAPI():
	api = tweepy.API(auth)
	print ("DEBUG: " + api.me().name + " is no logged in!")
	return api

def getAuth():
	return auth
