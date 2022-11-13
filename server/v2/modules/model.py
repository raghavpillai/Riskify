import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
 

def get_points(y_arr):
    x = 0
    x_arr = []
    y_arr = []
    for num in y_arr:
        x_arr.append(x)
        y_arr.append(num)
        x += 1
        print(num)


    x_a = np.array(x_arr).reshape(-1,1)
    y_a = np.array(y_arr).reshape(-1,1)

    # actually scuffed btw
    X_train,X_test,y_train,y_test = train_test_split(x_a,y_a,test_size=0.3,random_state=101)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    
    model = LinearRegression().fit(X_train,y_train)
    y_pred = model.predict(X_test)[:50]

    multi = 0
    prev = None
    bad_nums = []
    for num in y_pred:
        multi += 0.05
        if prev:
            num[0] = ((num[0] + prev) / 2)
        prev = num[0]
        bad_nums.append(num[0] + multi)

    return bad_nums