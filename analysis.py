import pandas as pd
import nltk # pip install nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
import re # regex
import itertools # to match date with text
from textblob import TextBlob # pip install textblob
import matplotlib.pyplot as plt

# get csv file
COLUMNS = ['UserScreenName', 'UserName', 'Timestamp', 'Text', 'Embedded_text', 'Emojis', 'Comments', 'Likes', 'Retweets', 'Image link', 'Tweet URL']
ENCODING = "utf-8"

pos_tweets = 0
neu_tweets = 0
neg_tweets = 0

df = pd.read_csv('outputs/newTwitterData.csv', encoding=ENCODING, names=COLUMNS)

dataDictionary = {} # to keep track of sentiment and the date related to it

sia = SentimentIntensityAnalyzer()

def clean_tweet(t):
    """Cleans up the tweet to remove extra symbols and links to make it easier to analyze"""
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(t)).split())

def get_sentiment(tweet, useBlob):
    """Uses TextBlob to analyze the sentiment of the passed tweet"""
    if useBlob:
        return TextBlob(clean_tweet(tweet)).sentiment.polarity
    return sia.polarity_scores(tweet)["compound"]

def clean_date(d):
    tempstr = d.split("-")
    return tempstr[1] + " " + tempstr[2][:2]

for (text, dateCol) in zip(df.loc[:,'Embedded_text'], df.loc[:,'Timestamp']):
    if text == "Embedded_text":
        continue # for some reason it grabs the header row too, so this skips it

    sentiment = get_sentiment((clean_tweet(text)), False)
    dc = clean_date(dateCol)
    
    if dc not in dataDictionary.keys():
        dataDictionary.update({dc : sentiment})
    else:
        dataDictionary[dc] += sentiment

    if sentiment > 0:
        pos_tweets += 1
    elif sentiment == 0:
        neu_tweets += 1
    else:
        neg_tweets += 1    

print("postive: " + str(pos_tweets) + "\nneutral: " + str(neu_tweets) + "\nnegative: " + str(neg_tweets))
print(dataDictionary)

x = list(dataDictionary.keys())
y = list(dataDictionary.values())

plt.bar(range(len(dataDictionary)), y, tick_label=x)

plt.xticks(range(0, len(x)+1, 7))
plt.title("Sentiment regarding Elon Musk")
plt.xlabel("Date (2022)")
plt.ylabel("Sentiment (higher is better/postive)")

plt.show()