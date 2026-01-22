import tweepy
import pandas as pd

BEARER_TOKEN = "PASTE_YOUR_BEARER_TOKEN_HERE"

client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = "AI OR Data Science OR Python lang:en"

response = client.search_recent_tweets(
    query=query,
    max_results=100,
    tweet_fields=["text"]
)

tweets = [tweet.text for tweet in response.data]

df = pd.DataFrame(tweets, columns=["text"])
df.to_csv("tweets.csv", index=False)

print("Tweets collected:", len(df))
