import numpy as np
import pandas as pd
from pandas import Series,DataFrame

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

data=pd.read_csv('dataset.csv')

X=data.drop('Target',axis=1)
Y=data['Target']

X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X,Y)

logregmodel=LogisticRegression().fit(X_train,Y_train)
lrscore=logregmodel.score(X,Y)
Y_pred = logregmodel.predict(X_test)
lraccuracy=metrics.accuracy_score(Y_test,Y_pred)
