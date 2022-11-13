import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

from sklearn.neighbors import KNeighborsRegressor
 

def get_change(current, previous):
    if current == previous:
        return 1
    try:
        return 1 + ((current - previous) / previous)/100
    except ZeroDivisionError:
        return 1

def get_points(def_arr):
    last = def_arr[0]
    changes = []
    for i in def_arr:
        ch = get_change(i, last)
        changes.append(ch)
        last = i

    nums = []
    last = def_arr[0]
    for i in range(0,9125):
        try:
            multi = changes[i/350]
        except:
            multi = changes[-1]
        #print(multi)
        new = last * multi
        last = new
        if last == 0:
            last+=1
        nums.append(new) 
        
    newnums = []
    for i in range(25):
        newnums.append(nums[i*364])
    #print("FFFFFFFFFFFFF")
    
    return newnums