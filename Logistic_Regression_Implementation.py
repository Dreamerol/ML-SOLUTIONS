import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
X_train = data[['feature1', 'feature2']].values
y_train = data['target'].values

m, n = X_train.shape
#n - the number of input features
#m - number of samples

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

def cost_function(X,y,W,b):
  cost_sum = 0
  for i in range(m):
    z = np.dot(W, X[i])
    g = sigmoid(z)

    cost_sum += -y[i]*np.log(g) - (1 - y[i])*(np.log(1-g))

  return cost_sum / m


#function for calculation of teh derivative of the loss function
#d'[x] = d[x].[1-d[x]] derivative of sigmoid
#-yi.log[gi] - [1-yi].log[1-gi] -> -yi/gi . g'i - [1-yi]/[1-gi]
#[gi-yi]/[gi.[1-gi]] .derivative_sigmoid_of_gi which is gi.[1-gi]
#and then we get the [xij.wij]'wij we will get the xij when differentianting by weights
#if we differentiate by b we will get just one

def gradient_function(X,y,W,b):
  grad_w = np.zeros(n)
  #we want to find the gradient for each of the parameters/weights wij
  grad_b = 0

  for i in range(n):
    z = np.dot(w, X[i]) + b
    g = sigmoid(z)
        
    grad_b += g - y[i]
    for j in range(n):
      #when we compute the derivative by each weight - w1,..wn
      #we will get the xi1, xi2, ... xin
      grad_w[j] += (g - y[i]) * X[i][j]

  grad_b /= m
  grad_w /= m

  return grad_b, grad_w

def gradient_descent(X, y, alpha, iterations):
  w = np.zeros(n)
  b = 0

  for i in range(iterations):
    grad_b, grad_w = gradient_function(X, y, w, b)
    w -= alpha * grad_w
    b -= alpha * grad_b

    if i % 100 == 0:
      print(f"Iteration {i}, Cost {cost_function(X,y,w,b)}")

  return w, b

def predict(X,w,b):
  preds = np.zeros(n)

  for i in range(n):
    z = np.dot(w, X[i]) + b
    g = sigmoid(z)

    preds[i] = 1 if g >= 0.5 else 0

  return preds

learning_rate = 0.1
iterations = 4555

final_w, final_b = gradient_descent(X_train, y_train, learning_rate, iterations)
predictions = predict(X_train, final_w, final_b)
accuracy = np.mean(predictions == y_train) * 100
print(accuracy) 
