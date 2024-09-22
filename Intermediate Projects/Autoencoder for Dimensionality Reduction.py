import numpy as np
from keras.models import Sequential
from keras.layers import Dense

data = np.random.rand(1000, 20)
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(20,)))
model.add(Dense(20, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(data, data, epochs=10)
