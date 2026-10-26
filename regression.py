import numpy as np
from sklearn.linear_model import LinearRegression
 
X = np.array([100, 150, 200, 250, 300])
X = X.reshape(-1, 1)
y = np.array([29, 41, 53, 66, 78])
 
model = LinearRegression()
model.fit(X, y)
print(model.coef_, model.intercept_)
print(model.predict([[180]]))
