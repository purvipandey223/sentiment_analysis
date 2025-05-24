import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "Stray Kids since:2024-01-01"
max_tweets = 1000

tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if i >= max_tweets:
        break
    tweets.append([tweet.date, tweet.user.username, tweet.content])

df = pd.DataFrame(tweets, columns=["Date", "Username", "Content"])
df.to_csv("straykids_tweets.csv", index=False)
