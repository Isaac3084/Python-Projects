import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt

data = pd.read_csv('time_series_data.csv')
model = ARIMA(data['value'], order=(5, 1, 0))
model_fit = model.fit(disp=0)
forecast = model_fit.forecast(steps=10)
plt.plot(forecast)
plt.show()
