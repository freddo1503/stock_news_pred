import pandas as pd
import numpy as np
import pymysql
import os
from .utils import simple_time_tracker
from dotenv import load_dotenv


#load environment variable
load_dotenv()

def connect_to_db():
    """Function to make the connection with\
    the database and return the cursor"""
    connection = pymysql.connect(
        host=os.environ.get('DB_HOST'), 
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD'),
        db=os.environ.get('DB_NAME')
    )
    return connection

@simple_time_tracker
def get_tweet_data(cursor):
    """Function to get the data from\
       the tweets table in the database"""
    # Create a new query that selects the entire contents of 'ticker'
    sql = "SELECT ticker, `date`, tweet FROM tweets"
    cursor.execute(sql)
    return pd.DataFrame(cursor.fetchall(), columns=['ticker', 'date', 'tweet'])

@simple_time_tracker
def upload_tweet_sentiment(df):
    """Function to upload the sentiment tweet prediction\
        in the database\
        in predictionmodel table\
        in the tweet_api_sentiment column"""
    #connect to the dB
    connection = connect_to_db()
    cursor = connection.cursor()

    #transform the DataFrame in a list of list
    tweet_list = list(df[['tweet_sentiment','date', 'ticker']].values)
    tweet_list = np.array(tweet_list)
    tweet_list = tweet_list.tolist()

    for tweet_sentiment, date, ticker in tweet_list:
        try:
            #If the prediction does not yet exist, it is inserted into the database,
            #otherwise it is updated
            sql = """INSERT INTO prediction (tweet_api_sentiment, `date`, ticker) \
                    VALUES (%s, %s, %s)"""
            #Values you want to insert
            values = (tweet_sentiment, date, ticker)
            cursor.execute(sql, values)
            connection.commit()

        except pymysql.Error as err:
            if err.args[0] == 1062:
                print('Duplicate entry, updating the values')
                #SQL query
                sql = """UPDATE prediction SET tweet_api_sentiment=%s WHERE `date`=%s AND ticker=%s"""
                #Values you want to insert
                values = (tweet_sentiment, date, ticker)
                cursor.execute(sql, values)
                connection.commit()

if __name__ == "__main__":
    print('test')
    test_list = [['tweet goood', '2012-01-01', 'GOOGL'], 
                ['tweet goood', '2015-01-02', 'GOOGL']]
    df = pd.DataFrame(test_list, columns=['tweet_sentiment','date', 'ticker'])
    upload_tweet_sentiment(df)
    