# Step 1: Import libraries
import numpy as np
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 2: Load dataset
iris = load_iris()
X = iris.data        # features: sepal length, width, etc.
y = iris.target      # labels: 0=setosa, 1=versicolor, 2=virginica

# Step 3: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train logistic regression WITHOUT scaling
model1 = LogisticRegression(max_iter=200)
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)
print("Accuracy without scaling:", accuracy_score(y_test, pred1))

# Step 5: Apply StandardScaler
scaler = StandardScaler()          # create the scaler
X_train_scaled = scaler.fit_transform(X_train)  # fit on train data & transform it
X_test_scaled = scaler.transform(X_test)        # use same scaler for test data

# Step 6: Train logistic regression WITH scaling
model2 = LogisticRegression(max_iter=200)
model2.fit(X_train_scaled, y_train)
pred2 = model2.predict(X_test_scaled)
print("Accuracy with StandardScaler:", accuracy_score(y_test, pred2))
