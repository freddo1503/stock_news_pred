"""Here we code our notebook process to traine the LSTM"""
#from pymysql import cursors
#from stockLstmModel.data import get_stocksprice_data, upload_LSTM_prediction, connect_to_db
#from stockLstmModel.utils import simple_time_tracker

#Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from google.cloud import storage
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.callbacks import EarlyStopping


#@simple_time_tracker

# Function to get data
def get_stock_data_from_gcp(nrows=10000,
                            local=False,
                            optimize=False,
                            **kwargs):
    """method to get the training data (or a portion of it) from google cloud bucket"""
    # Add Client() here
    client = storage.Client()
    if local:
        path = "data/data_data_10Mill.csv"
    else:
        path = "gs://stock-news-pred-bucket/amazon_stock_price.csv"
    df = pd.read_csv(
        path)  #add nrows after if you want to select a specific number of row
    return df


# Function to scale data
def scale_stock_data(df, ticker):
    X = df[[ticker]]
    sc = MinMaxScaler().fit(X)
    X_sc = sc.fit_transform(X)
    return sc, X_sc

# Function to split scaled data
def split_stock_data(X_sc, train_size):
    index = round(train_size * X_sc.shape[0])
    X_sc_train = X_sc[:index]
    X_sc_test = X_sc[index:]
    return X_sc_train, X_sc_test

# Function to reshape scaled train data
def reshape_train_data(X_sc_train, obs):
    X_train = []
    y_train = []
    for i in range(obs, X_sc_train.shape[0]):
        X_train.append(X_sc_train[i - obs:i, 0])
        y_train.append(X_sc_train[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    return X_train, y_train

# Function to reshape scaled test data
def reshape_test_data(X_sc_test, obs):
    X_test = []
    y_test = []
    for i in range(obs, X_sc_test.shape[0]):
        X_test.append(X_sc_test[i - obs:i, 0])
        y_test.append(X_sc_test[i, 0])
    X_test, y_test = np.array(X_test), np.array(y_test)
    X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
    return X_test, y_test

# Function to build the lstm model
def lstm_model():
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Function to train the model
def train_model(X_train, y_train):
    model = lstm_model()
    es = EarlyStopping(patience=30, restore_best_weights=True)
    model.fit(X_train,
              y_train,
              validation_split=0.2,
              epochs=100,
              batch_size=32,
              callbacks=[es],
              verbose=1)
    return model

# Function to predict results
def predict_model(ticker):
    sc, X_sc = scale_stock_data(df, ticker)
    X_sc_train, X_sc_test = split_stock_data(X_sc, 0.8)
    X_train, y_train = reshape_train_data(X_sc_train, 30)
    X_test, y_test = reshape_test_data(X_sc_test, 30)
    model = train_model(X_train, y_train)
    predicted_stock_price = model.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    return predicted_stock_price

# Function to save model.joblib
#def save_model():
    #joblib.dump(model, 'lstm_model_stock_price.joblib')



if __name__ == "__main__":
    #connection = connect_to_db()
    #cursors = connection.cursor()

    df = get_stock_data_from_gcp()
    X = df[['AMZN']]
    prediction = predict_model('AMZN')
    print(prediction)
