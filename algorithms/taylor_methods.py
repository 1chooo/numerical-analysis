# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:28:08 2019

@author: user
"""
import math
def f(x,y):
    y1 = y-t*t+1
    return y1
def f1(t):
    return (t+1)*(t+1)-0.5*math.exp(t)

    
b = 2
a = 0
N = 10
a1 = 0.5
h = (b-a)/N
t = a
w = a1
print(t,a1)
for i in range(1,N+1):
    w = w + h*((1+(h/2))*(w-t*t+1)-h*t)
    t = a+i*h
    err = 0.1*((0.5*math.exp(2))-2)*(math.exp(t)-1)
    error = abs(f1(t)-w)
    print(t,w,error)
