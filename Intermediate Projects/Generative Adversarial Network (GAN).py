import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Reshape

generator = Sequential()
generator.add(Dense(256, input_dim=100))
generator.add(Reshape((16, 16, 1)))
