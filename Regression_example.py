import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LogisticRegression

x = np.linspace(-5, 5, 40)
y = 5 * x + 6
y_err = np.random.normal(scale = 55, size = 40)
#gives random points size - the number of points
y += y_err

plt.scatter(x,y)
model = LinearRegression()
model.fit(x.reshape(-1,1), y)
print(model.coef_, model.intercept_)
#model_coef - we get the coef in front of x
#model_intercept - we get the free coef


y_tilda = model.predict(x.reshape(-1,1)) # gives us the predicted y_values
plt.scatter(x,y,color="blue")
plt.plot(x, y_tilda, color="red")

#model.score -> R-squared score - 1 - if the model predicts everthing right
#if it is under zero - the model behaves really badly
model.score(x.reshape(-1, 1), y)
model.predict([[5]]) 

scaler = MinMaxScaler()
#-1 -> in reshape fnction means gets how many rows
x_transformed = scaler.fit_transform(x.reshape(-1,1))
plt.scatter(x_transformed, y_tilda)
#MinMax scaler -> interval -> [0,1] ->little numbers -> more faster

scaler.inverse_transform(x_transformed)
#invert the transformation 

reg = LinearRegression()
reg.fit([[0,0], [1,1], [2,2]], [0,1,2])
print(reg.coef_, reg.intercept_)
#creating a model for two variables f(x1,x2) = a1.x1 + a2.x2 + b


#--------------------------------------------------------------------------------------
#the dependency od tha differnet variables is in the form of curve
#Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
X = np.random.rand(20, 1) * 5
y = 1 + 2*X + 3*X**2 + np.random.rand(20, 1)
#y = 1 + 2x + 3x^2 + noise
poly = PolynomialFeatures(degree=2)
#we create a basis from second degree -> [1, x, x^2]
#then we pass it az multiple params for our linear regression model
#a.1 + b.x +...
X_poly = poly.fit_transform(X)
lin = LinearRegression()
lin.fit(X_poly, y)
#we find the coeffs
print(lin.coef_, lin.intercept_)

X2 = np.array([
  [1,2],
  [3,4],
  [5,6]
])

z = np.array([5,3,5])
# z = a0.x + a1.y + a2.x^2 + a3.y^2 +a4.x.y / multiplication of each pair it represents
# the reationship of the variables
X_poly_two_params = poly.fit_transform(X2)
lin.fit(X_poly_two_params, z)
print(lin.coef_, lin.intercept_)

#-------------------------------------------------------------------------------------------------------------
#Logistic Regression - separating into classes - but we need  evenly distributed data
#predicting a chance a student passes 1 based on the studying hours 
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])
model = LogisticRegression()
model.fit(X, y)
X_test = (np.random.rand(20) * 3).reshape(-1, 1)

y_prob = model.predict(X_test)
print(y_prob)

