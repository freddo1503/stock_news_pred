import pandas as pd
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


def get_stocksentiment_data():
    """Function to get the data from\
       the predictionmodel table in the database"""
    pass

def upload_stockprice_prediction():
    """Function to upload the stock prices with the sentiment\
        in the database\
        in predictionmodel table\
        in stockprice_prediction column"""
    pass

if __name__ == "__main__":
    print('test')
    