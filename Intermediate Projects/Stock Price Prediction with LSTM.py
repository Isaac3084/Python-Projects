import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense

data = pd.read_csv('stock_prices.csv')
X = data['Open'].values
X = X.reshape(-1, 1)
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, epochs=10)
