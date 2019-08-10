#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('stir.csv')
X = dataset.iloc[:, 0:3].values
y1 = dataset.iloc[:, 3].values#y1= ultimate tensile strength
y2 = dataset.iloc[:, 4].values#y2=tensile elongation %
y1=np.reshape(y1, (-1,1))
y2=np.reshape(y2, (-1,1))

# Feature Scaling
from sklearn.preprocessing import MinMaxScaler
scaler_x = MinMaxScaler()
scaler_y1 = MinMaxScaler()
scaler_y2 = MinMaxScaler()
print(scaler_x.fit(X))
xscale=scaler_x.transform(X)
print(scaler_y1.fit(y1))
yscale1=scaler_y1.transform(y1)
print(scaler_y2.fit(y2))
yscale2=scaler_y2.transform(y2)

#importing tensorflow
import tensorflow as tf

# Initialising the ANN
regressor = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer
regressor.add(tf.keras.layers.Dense(units = 3, kernel_initializer='normal', activation = 'relu', input_dim = 3))

# Adding the second hidden layer
regressor.add(tf.keras.layers.Dense(units = 3, activation = 'relu'))

# Adding the third hidden layer
regressor.add(tf.keras.layers.Dense(units = 3, activation = 'relu'))

# Adding the output layer
regressor.add(tf.keras.layers.Dense(units = 1, activation = 'linear'))

# Compiling the ANN
regressor.compile(optimizer = 'adam', loss = 'mse', metrics = ['mse','mae'])

#Fitting the ANN to the Training set for tensile strength
regressor.fit(xscale, yscale1, batch_size = 3, nb_epoch = 760)

#testing data
x_test=np.array([[1700,60,6]])
xtestscale=scaler_x.transform(x_test)

# Predicting tensile strength results
y_pred1= regressor.predict(xtestscale)#predicted ultimate tensile strength
y_pred1 = scaler_y1.inverse_transform(y_pred1)

#Fitting the ANN to the Training set for tensile elongation
regressor.fit(xscale, yscale2, batch_size = 2, nb_epoch = 1000)

# Predicting tensile elongation results
y_pred2= regressor.predict(xtestscale)#predicted tensile elongation
y_pred2 = scaler_y2.inverse_transform(y_pred2)
 
