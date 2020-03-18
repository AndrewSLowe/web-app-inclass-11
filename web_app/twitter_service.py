import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
print("AUTH", auth)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
print("API", api)
# # print(dir(api))

user = api.get_user('Chrisalbon')
print('USER', user)
print(user.screen_name)
print(user.name)
print(user.followers_count)
# dir(user) => can see followers counts, and tons of other shit!

breakpoint()

# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print(type(tweet))
#     print(tweet.text)
#     print('----------------------')