# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:45:44 2019

@author: user
"""

import numpy as np

x =np.array([1,2,3,4,5,6,7,8,9,10])
y =np.array([1.3,3.5,4.2,5.0,7.0,8.8,10.1,12.5,13.0,15.6])
x2 = np.square(x)
xy = [0]*10
m = 10
for i in range(10):
    xy[i] = x[i]*y[i]
a0 = (sum(x2)*sum(y)-sum(xy)*sum(x))/(m*sum(x2)-(sum(x))**2)
a1 = (m*sum(xy)-sum(x)*sum(y))/(m*sum(x2)-(sum(x))**2)

print(a1,a0)
