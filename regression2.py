import numpy as np
 
X_train = np.array([
    [1, 1], [1, 1], [1, 1],
    [1, 0], [1, 0], [0, 1],
    [1, 1], [1, 0], [0, 0],
    [0, 0], [0, 0], [0, 0]
])

y_train = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0])

X_test = np.array([[1, 1], [1, 0]])

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
 
model = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)
model.fit(X_train, y_train)
 
p = model.predict_proba(X_test)[:, 1]
alerts = (p >= 0.50).astype(int)
 
print(p)
print(alerts)
