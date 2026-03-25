import numpy as np
#why SVM - prevents overfitting 
#we want the distance between the line and the closest data points to be maximum
#so the model to be not sensitive on noise

class SupportVectorMachine:
  def __init__(self, learning_rate=0.1, lambda_params=0.1,n_iters=1000):
    self.learning_rate = learning_rate
    self.lambda_params = lambda_params
    self.n_iters = n_iters
    self.W = None
    self.b = None

  def fit(self, X, y):
    n_samples, n_features = X.shape
    #scaling the y values between of y between negative one and one
    #that are our support vector lines, so to make the classification and the 
    #linear separation of the classes more clear 
    y_ = np.where(y <= 0, -1, 1)  

    #we can present the point x as a vector[x1,x2..]
    self.W = np.zeros(n_features)
    self.bias = 0 

    for _ in range(n_iters):
      for idx, x_i in enumerate(X):
        condition = y[idx] * np.dot(x_i, self.W) - self.bias >= 1
        #we have two scenarios - yi.f[xi] bigger than one - this means the
        #prediction is right so we have no loss/zero/ and we have left with only
        #one half  a||w||^2
        if condition:
          #so the derivative will be lambda/a/.w
          self.W -= learning_rate *( 2 * self.lambda_params * self.W)
        else:
          #the second scenario is yi.f is less than one , so the model is not right
          #so the loss will look like -> 1 - yi.[wxi-b] + the reg index
          #so the derivative will look like the same as the positive scebario -minus
          self.W -= learning_rate *( 2 * self.lambda_params * self.W - np.dot(x_i, y[idx]))
          #the derivative by b is -yi.[-1] -> yi
          self.bias -= learning_rate * y[idx]
             
      def predict(self, X):
        linear_output = np.dot(X, self.W) - self.bias 
        return np.sign(linear_output)



