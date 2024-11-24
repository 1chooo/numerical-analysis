# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import math
def f(x,y):
    y1 = y-t*t+1
    return y1
b = 2
a = 0
N = 10
a1 = 0.5
h = (b-a)/N
t = a
w = a1
print(t,a1)
for i in range(1,N+1):
    w = w + h*f(t,w)
    t = a+i*h
    err = 0.1*((0.5*math.exp(2))-2)*(math.exp(t)-1)
    print(t,w,err)
    