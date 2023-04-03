import nltk # pip install nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

import pandas as pd
import re # regex

# get csv file
COLUMNS = ['UserScreenName', 'UserName', 'Timestamp', 'Text', 'Embedded_text', 'Emojis', 'Comments', 'Likes', 'Retweets', 'Image link', 'Tweet URL']
ENCODING = "utf-8"

pos_tweets = 0
neu_tweets = 0
neg_tweets = 0

df = pd.read_csv('outputs/newTwitterData.csv', encoding=ENCODING, names=COLUMNS)

sia = SentimentIntensityAnalyzer()

def clean_tweet(t):
    """Cleans up the tweet to remove extra symbols and links to make it easier to analyze"""
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(t)).split())

def get_sentiment(tweet):
    """Uses NLTK to analyze the sentiment of the passed tweet"""
    return sia.polarity_scores(tweet)["compound"]

for text in df.loc[:,'Embedded_text']:
    sentiment = get_sentiment((clean_tweet(text)))
    if sentiment > 0:
        pos_tweets += 1
    elif sentiment == 0:
        neu_tweets += 1
    else:
        neg_tweets += 1

print("postive: " + str(pos_tweets) + "\nneutral: " + str(neu_tweets) + "\nnegative: " + str(neg_tweets))