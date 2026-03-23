import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("data.csv")
X = data.drop(columns=['id', 'diagnosis'])
y = data['diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


class NaiveBayes:
  def fit(self, X_train, y_train):
    self.classes = np.unique(y_train)
    self.priors = [len(y_train[y_train == c]) / len(y_train) for c in self.classes]

    self.means = [X_train[y_train == c].mean() for c in self.classes]
    #calculate the mean per feature for all the matching rows of this class
    self.stds = [X_train[y_train == c].std() for c in self.classes]

  def compute_likelihood(self, row, class_idx):
    likelihood = 1
    for feature in row.index:
      mean = self.means[class_idx][feature]
      std = self.stds[class_idx][feature]
      #so for each feature we calculate the probability for each feature
      likelihood *= (1/(np.sqrt(2*np.pi) * std)) * np.exp((-(row[feature]-mean)**2)/ (2*std**2))
    return likelihood

  def predict(self, X):
    y_pred = []
    for _, row in X.iterrows():
      posteriors = []
      for i in range(len(self.classes)):
        likelihood = self.compute_likelihood(row, i)
        posteriors.append(likelihood * self.priors[i])
        #self.priors - gives us the probablities of class Ci 

      #for each row we get the index of the class with the biggest probability
      y_pred.append(self.classes[np.argmax(posteriors)])
    return np.array(y_pred)

nb = NaiveBayes()
nb.fit(X_train, y_train)
predictions = nb.predict(X_test)

accuracy = np.mean(predictions == y_test) * 100
print(accuracy)
