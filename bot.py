import tweepy
import validators 

with open('keys/twitterKey', 'r') as file:
    key = file.read()
    print(key)
with open('keys/twitterSecret', 'r') as file:
    secret = file.read()
    print(secret)
with open('keys/twitterAccessKey', 'r') as file:
    accessKey = file.read()
    print(accessKey)
with open('keys/twitterAccessSecret', 'r') as file:
    accessSecret = file.read()
    print(accessSecret)

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

tweets = api.user_timeline(screen_name="elonmusk",
                           count=200,
                           include_rts=False,
                           tweet_mode='extended'
                           )

for tweet in tweets:
    tweetLowerCase = tweet.full_text.lower()
    #print(tweetLowerCase)
    if (tweetLowerCase.find("shiba") >= 0):
        print("ID: {}".format(tweet.id))
        print(tweet.created_at)
        print(tweet.full_text)
        print("\n")

