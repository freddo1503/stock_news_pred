"""Here we code our notebook process"""
import newsSentimentModel
from flair.models import TextClassifier
from flair.data import Sentence
import pandas as pd

df = newsSentimentModel.data.get_news_data()

def classify_sentence(X):
    sentence = Sentence(X)
    classifier.predict(sentence)
    return sentence.labels

#instantiate the classifier
classifier = TextClassifier.load('en-sentiment')
df["sentiment"] = df["title"].apply(classify_sentence)


# preprocess the data to aggregate the news sentiment to one per day
#create a function to get out the boolean result per row
def preprocess_sentiment(X):
    return X.split()[0][1:]

def preprocess_sentiment_data(df):
    df["sentiment_result"] = df["sentiment"].apply(preprocess_sentiment)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    df = df.sort_values(by="date")
    #create a new column positive
    df["positive"] = df["sentiment_result"].apply(lambda X: 1
                                                if X == "POSITIVE" else 0)
    #create a new column negative
    df["negative"] = df["sentiment_result"].apply(lambda X: 1
                                                if X == "NEGATIVE" else 0)
    #group by per date and ticker
    df_sentiment_count = df.groupby(by=["date", "ticker"]).agg(sum)
    #reset index to have date per row
    df_sentiment_count.reset_index(drop=False, inplace=True)
    #create a new column to
    df_sentiment_count["majority"] = df_sentiment_count[
        "positive"] - df_sentiment_count["negative"]
    return df

#Alternative: percentage of good news

#df_sentiment_count["majority"] = df_sentiment_count["positive"] / (
#    df_sentiment_count["positive"] + df_sentiment_count["negative"])

# What to hand to upload function?@Freddie

#updating the csv_news_sentiment
newsSentimentModel.data.upload_csv_sentiment()
