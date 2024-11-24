# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import math


def d(x):
    return x*x
def c(x):
    return x*x*x
def f(x,y):
    return math.exp(y/x)
b = 0.5
a = 0.1
n = 1000
m = 1000
h = (b-a)/n
J1 = 0
J2 = 0
J3 = 0

for i in range(n):
    x = a + i*h
    HX = (d(x)-c(x))/m
    K1 = f(x,c(x))+f(x,d(x))
    K2 = 0
    K3 = 0
    for j in range(m):
        y = c(x)+j*HX
        Q = f(x,y)
        if (j%2==0):
            K2 = K2+Q
        else:
            K3 = K3+Q
    L = (K1+2*K2+4*K3)*HX/3
    if (i == 0 ):
        J1 = J1 + L
    if (i == n):
        J1 = J1 + L
    if (i%2 == 0):
        J2 = J2+L
    else:
        J3 = J3+L
J = h*(J1+2*J2+4*J3)/3
print(J)