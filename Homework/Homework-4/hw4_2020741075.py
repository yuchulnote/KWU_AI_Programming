# -*- coding: utf-8 -*-
"""Samsung.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Er4r_qEXtfja3RNA8ZgqtIysaWoN20I1
"""

from google.colab import drive
drive.mount('/content/gdrive', force_remount=False)

import os
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense 
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

folder = "AI_Programming"
project_dir = "dnn"

base_path = Path("/content/gdrive/My Drive/")
project_path = base_path / folder / project_dir
os.chdir(project_path)
for x in list(project_path.glob("*")):
    if x.is_dir():
        dir_name = str(x.relative_to(project_path))
        os.rename(dir_name, dir_name.split(" ", 1)[0])
print(f"현재 디렉토리 위치: {os.getcwd()}")

data = pd.read_csv("/content/gdrive/My Drive/AI_Programming/dnn/samsung.csv")

print(data)

col = data[['close', 'start', 'high', 'low', 'volume', 'transactionPrice', 'capitalization']]

MMS = MinMaxScaler(feature_range=(0,1))
MMS_fit = MMS.fit(col)
row = MMS.transform(col)

df = pd.DataFrame(row, columns=col.columns)
print(df)

df_corr = df.corr()
df_corr_sort = df_corr.sort_values('close', ascending = False)
df_corr_sort['close'].head(10)

X = df.iloc[:, :]
# print("X모양", X)

y = df.iloc[:, 0]
# print("y모양", y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, shuffle = True, random_state=777)

model = Sequential()
model.add(Dense(128, input_dim = 7, activation = 'relu'))
# model.add(Dense(128, activation = 'relu'))
model.add(Dense(64, activation = 'relu'))
# model.add(Dense(32, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(1))
model.summary

model.compile(loss = 'mean_squared_error', optimizer = 'adam', metrics = ['MSE'])

early_stopping_callback = EarlyStopping(monitor = 'val_loss', patience = 20)
modelpath = '/content/gdrive/My Drive/AI_Programming/dnn/samsung_best_model.hdf5'
checkpointer = ModelCheckpoint(filepath = modelpath, monitor = 'val_loss', verbose = 0, save_best_only = True)

history = model.fit(X_train, y_train, epochs = 1000, batch_size = 32, validation_split = 0.25, verbose = 1, callbacks = [early_stopping_callback, checkpointer])

list_y_test = np.array(y_test)

real_prices = []
pred_prices = []
X_num = []
n_iter = 0
Y_prediction = model.predict(X_test).flatten()

Max = 80500
Min = 52500

close_max = list_y_test*(Max - Min)+Min
close_min = Y_prediction*(Max - Min)+Min

for i in range(50):
  real = close_max[i]
  prediction = close_min[i]
  print('Real price: {}, Expected price: {}'.format(real, prediction))
  real_prices.append(real)
  pred_prices.append(prediction)
  n_iter = n_iter + 1
  X_num.append(n_iter)
  
plt.plot(X_num, pred_prices, label = 'Expected')
plt.plot(X_num, real_prices, label = 'Real')
plt.legend()
plt.show()