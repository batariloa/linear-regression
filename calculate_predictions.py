from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt


raw_data = pd.read_csv('generisani_podaci.csv')

data1 = raw_data[['cs_101_ocena']]

data2 = raw_data[['cs_115_izostanci']]

data3 = raw_data[['cs_101_ocena', 'ma_101_ocena', 'cs_115_izostanci']]

y = raw_data['cs_115_ocena']

fig = plt.figure()


def show_linear_regression_predictions(x, y, subplot_coord):
    regressor = LinearRegression()

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=0)
    regressor.fit(X_train, y_train)  # tain the algorithm

    y_pred = regressor.predict(X_test)

    subplot = fig.add_subplot(subplot_coord)
    subplot.scatter(X_train, y_train, color='gray')
    subplot.plot(X_test, y_pred, 'r')

    greska = metrics.mean_absolute_error(y_test, y_pred)

    print('Greska za dataset je ', greska)


show_linear_regression_predictions(data1, y, 221)
linear_regression(data2, y, 222)


plt.show()
