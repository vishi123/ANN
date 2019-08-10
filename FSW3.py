#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('stir.csv')
X = dataset.iloc[:, 0:3].values
y1 = dataset.iloc[:, 3].values
y2 = dataset.iloc[:, 4].values
y1=np.reshape(y1, (-1,1))
y2=np.reshape(y2, (-1,1))
dataset= dataset.drop(axis=1, columns=["Unnamed: 5"])


#Feature Scaling
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


# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(xscale, yscale1)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xscale, yscale1)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xscale, yscale1)

#fitting the DTregression model to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(xscale, yscale1) 

#fitting the RFregression model to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=600, random_state=0)
regressor.fit(xscale, yscale1) #for tensile strength

#fitting the RFregression model to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor2=RandomForestRegressor(n_estimators=600, random_state=0)
regressor2.fit(xscale, yscale2) #for tensile elongation %

#testing data
x_test=np.array([[1700,60,6]])
xtestscale=scaler_x.transform(x_test)

# Predicting the Test set results for tensile strength
y_pred1= regressor.predict(xtestscale)
y_pred1=np.reshape(y_pred1, (-1,1))
y_pred1 = scaler_y1.inverse_transform(y_pred1) 

# Predicting the Test set results for tensile elongation
y_pred2= regressor2.predict(xtestscale)
y_pred2=np.reshape(y_pred2, (-1,1))
y_pred2 = scaler_y2.inverse_transform(y_pred2)



