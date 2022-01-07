import pandas as pd
import pymysql
import numpy as np
import os

from pymysql import connections
from .utils import simple_time_tracker
from dotenv import load_dotenv
import sys, traceback


#load environment variable
load_dotenv()

def connect_to_db():
    try:
        """Function to make the connection with\
        the database and return the cursor"""
        cursor = pymysql.cursors.DictCursor
        
        connection = pymysql.connect(
            host=os.environ.get('DB_HOST'), 
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            db=os.environ.get('DB_NAME'),
            cursorclass=cursor
        )
        print(connection)
        return connection
    except pymysql.err.OperationalError:
        print(traceback.format_exc())
    # or
        print(sys.exc_info()[2])


@simple_time_tracker
def get_news_data(cursor):
    """Function to get the data from\
       the newsapi table in the database"""

    # Create a new query that selects the entire contents of 'ticker'
    sql = "SELECT ticker, `date`, title, content FROM news"
    cursor.execute(sql)
    return pd.DataFrame(cursor.fetchall(), columns=[ 'ticker', 'date', 'title', 'content'])

@simple_time_tracker
def upload_news_sentiment(df):
    """Function to upload the sentiment news prediction \
        in the database\
        in predictionmodel table\
        in the tweet_api_sentiment column""" 
    #connect to the dB
    connection = connect_to_db()
    cursor = connection.cursor()

    #transform the DataFrame in a list of list
    news_list = list(df[['news_sentiment','date', 'ticker']].values)
    news_list = np.array(news_list)
    news_list = news_list.tolist()

    for news_sentiment, date, ticker in news_list:
        try:
            #If the prediction does not yet exist, it is inserted into the database,
            #otherwise it is updated
            sql = """INSERT INTO prediction (news_api_sentiment, `date`, ticker) \
                    VALUES (%s, %s, %s)"""
            #Values you want to insert
            values = (news_sentiment, date, ticker)
            cursor.execute(sql, values)
            connection.commit()

        except pymysql.Error as err:
            if err.args[0] == 1062:
                print('Duplicate entry, updating the values')
                #SQL query
                sql = """UPDATE prediction SET news_api_sentiment=%s WHERE `date`=%s AND ticker=%s"""
                #Values you want to insert
                values = (news_sentiment, date, ticker)
                cursor.execute(sql, values)
                connection.commit()

if __name__ == "__main__":
    connect_to_db()

    #test upload_news_sentiment 
    #print(upload_news_sentiment("2012-01-01", "GOOGL", "good sentiment22"))
