# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
import matplotlib.pyplot as plt

def f1(t,I1,I2):
    return -4*I1+3*I2+6
def f2(t,I1,I2):
    return -2.4*I1+1.6*I2+3.6

N = 100
m = 2
h = 0.1
t = a = 0
w = [0,0,0]
a1 = [0,0,0]
k1 = [0,0,0]
k2 = [0,0,0]
k3 = [0,0,0]
k4 = [0,0,0]
x1 = [0]*N
x2 = [0]*N
t1 = [0]*N
for i in range(1,N):
    t1[i] = t1[i-1]+ 0.1
for j in range(1,m):
    w[j] = a1[j]
print(t,w[1],w[2])
for i in range(1,N):
        k1[1] = h*f1(t,w[1],w[2])
        k1[2] = h*f2(t,w[1],w[2])
        k2[1] = h*f1(t+h/2,w[1]+0.5*k1[1],w[2]+0.5*k1[2])
        k2[2] = h*f2(t+h/2,w[1]+0.5*k1[1],w[2]+0.5*k1[2])
        k3[1] = h*f1(t+h/2,w[1]+0.5*k2[1],w[2]+0.5*k2[2])
        k3[2] = h*f2(t+h/2,w[1]+0.5*k2[1],w[2]+0.5*k2[2])
        k4[1] = h*f1(t+h,w[1]+k3[1],w[2]+k3[2])
        k4[2] = h*f2(t+h,w[1]+k3[1],w[2]+k3[2])
        w[1] = w[1]+(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        w[2] = w[2]+(k1[2]+2*k2[2]+2*k3[2]+k4[2])/6
        t = a+i*h
        x1[i] = w[1]
        x2[i] = w[2]
        print(t,w[1],w[2])
plt.plot(t1,x1)
plt.plot(t1,x2)
        
        
        