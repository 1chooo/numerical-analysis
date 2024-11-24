# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import math

b = 3.14159/2
a = 0
n = 4
h = (b-a)/n

def f(x):
    return math.sin(x)
XI0 = f(a)+f(b)
XI1 = 0
XI2 = 0
for i in range(1,n):
    X = a+i*h
    if i%2 ==0 :
        XI2 = XI2+f(X)
    else:
        XI1 = XI1+f(X)
XI = h*(XI0+2*XI2+4*XI1)/3
print (XI)