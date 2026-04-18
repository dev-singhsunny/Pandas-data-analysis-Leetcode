import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets = tweets[tweets['content'].apply(lambda x: True if len(x)> 15 else False)]
    return tweets[['tweet_id']]