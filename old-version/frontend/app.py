# pylint: disable-msg=C0103
"""This is the frontend of stock_news_pred"""

import datetime as dt
import streamlit as st
import pandas as pd
from dateutil.relativedelta import relativedelta
from api import connect_db


# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
# creation dt connection
pool = connect_db.init_db_connection()
connection = pool.connect()

# Perform API


# setup page
st.set_page_config(layout="wide")

# title page
st.title("Predict stock prices with sentiment analysis")

# Select parameters query
rows = pd.DataFrame(connection.execute("""SELECT * from ticker;""").fetchall())
ticker = st.selectbox("Ticker", rows)
date = st.date_input('Date', key='Date')
value = (date, ticker)

st.subheader(f"These are the news and tweets about {ticker} on {date}")
col1, col2, col3 = st.columns(3)
with col1:
    st.header('News')
    news = pd.DataFrame(connection.execute("""SELECT title, content, sentiment \
                                              FROM news \
                                              WHERE `date` = %s AND ticker = %s\
                                           """, value).fetchall(),
                        columns=['title', 'content', 'sentiment of the day'])
    st.dataframe(news[['title', 'sentiment of the day']])

with col2:
    st.header('Tweets')
    news = pd.DataFrame(connection.execute("""SELECT tweet, sentiment \
                                              FROM tweets \
                                              WHERE `date` = %s AND ticker = %s\
                                           """, value).fetchall(),
                        columns=['tweet', 'sentiment'])
    news['sentiment'] = news['sentiment'].str.slice(1, 9)
    st.dataframe(news)

with col3:
    st.header('Stock prices')

    # Range selector
    Value = (
        ticker,
        date - relativedelta(years=2),
        date + dt.timedelta(days=10)
    )

    query = """SELECT date, stock_price \
        FROM stocksprice \
        WHERE ticker = %s AND (`date` BETWEEN %s AND %s)"""

    stock = pd.DataFrame(connection.execute(query, value).fetchall(),
                         columns=['date', 'stock_price'])
    stock = stock.set_index('date')
    st.line_chart(stock)
    st.table(pd.DataFrame([[date - relativedelta(years=2), date, date + dt.timedelta(days=10)]],
                          columns=['start',
                                   'selected',
                                   'end'],
                          index=['date']))

st.header(f"Predictions with the LSTM model using 3 features for {ticker}")
st.subheader(
    "Historical stock prices, news sentiment analysis, tweets sentiment analysis")
query = """SELECT p.`date`, stock_price, next_day_pred \
       FROM prediction p INNER JOIN stocksprice s \
       ON s.`date` = p.`date` AND s.ticker = p.ticker \
       WHERE p.ticker = %s AND (p.`date` BETWEEN %s AND %s)"""

stock = pd.DataFrame(connection.execute(query, value).fetchall(),
                     columns=['date', 'stock price', 'prediction'])

stock.sort_values(by='date', ascending=False, inplace=True)
stock = stock.set_index('date')
stock['prediction'] = stock['prediction'].shift(-1)
stock['error'] = stock['prediction'] - stock['stock price']
stock['error rate (%)'] = stock['error'].abs() / stock['prediction'] * 100
st.line_chart(stock[['stock price', 'prediction']])
st.write(stock[['stock price', 'prediction', 'error rate (%)']])
