import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from sklearn.neighbors import KNeighborsRegressor
 
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    return b, a # return x, y intercept

def get_points(def_arr):
    x = 0
    x_arr = []
    y_arr = []
    for num in def_arr:
        x_arr.append(x)
        y_arr.append(num)
        x += 1

    x_a = np.array(x_arr).reshape(-1,1)
    y_a = np.array(y_arr).reshape(-1,1)
    
    # actually scuffed btw
    X_train,X_test,y_train,y_test = train_test_split(x_a,y_a)
    print(y_train)
    print(len(y_train))
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = LinearRegression().fit(X_train,y_train)
    y_pred = model.predict(X_test)
    #print(y_pred)

    multi = 0
    prev = None
    bad_nums = []
    for num in y_pred:
        if prev:
            num[0] = ((num[0] + prev) / 2)
        prev = num[0]
        bad_nums.append(num[0] + multi)
        multi += prev*0.02

    bad_nums[0] = def_arr[0]
    return bad_nums