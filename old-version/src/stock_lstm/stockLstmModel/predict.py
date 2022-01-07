#from .data import upload_LSTM_prediction
from keras.models import load_model
from trainer import scale_stock_data
from trainer import split_stock_data
from trainer import reshape_train_data
from trainer import reshape_test_data
from trainer import get_stock_data_from_gcp



model = load_model('lstm_model_stock_price.h5')

def predict_unscaled_data(X_test):
    predicted_stock_price = model.predict(X_test)
    predicted_stock_price = sc.inverse_transform(predicted_stock_price)
    return predicted_stock_price


#df_to_update = model.joblib(df)



if __name__ == "__main__":
    #upload_LSTM_prediction(df_to_update)
    df = get_stock_data_from_gcp()
    X = df[['AMZN']]
    sc, X_sc = scale_stock_data(df, 'AMZN')
    X_sc_train, X_sc_test = split_stock_data(X_sc, 0.8)
    X_train, y_train = reshape_train_data(X_sc_train, 30)
    X_test, y_test = reshape_test_data(X_sc_test, 30)
    y_pred = predict_unscaled_data(X_test)
    print(y_pred)
