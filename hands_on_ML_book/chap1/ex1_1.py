import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor


data_root="https://github.com/ageron/data/raw/main/"

life_sat= pd.read_csv(data_root+ "lifesat/lifesat.csv")

X= life_sat[["GDP per capita (USD)"]].values

y= life_sat[["Life satisfaction"]].values

life_sat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")

plt.axis([23_500, 62_500, 4, 9])
plt.show()
# model= LinearRegression()
model = KNeighborsRegressor(n_neighbors=3)
model.fit(X,y)
X_new= [[33_442.8]] #cho du doan
print(model.predict(X_new))

