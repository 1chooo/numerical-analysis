# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

a = [[1,1,0,3,4],[2,1,-1,1,1],[3,-1,-1,2,-3],[-1,2,3,-1,4]]
A = []
n = 4
x = np.zeros(n,float)
m = np.zeros((4,5),float)
def S(a,x,i,n):
    s = 0 
    for j in range(i+1,n):
        s = s+a[i][j]*x[j]
    return s
def f(a,A,n,x,m):
    for i in range(0,n-1):
        for p in range(i,n):
            if a[p][i]!= 0:
                break
            if p ==n :
                return
        if p!=i:
            A = a[p]
            a[p]=a[i]
            a[i] = A
        for j in range(i+1,n):
            m[j][i] = a[j][i]/a[i][i]
            for k in range(len(a[j])):
                a[j][k] = a[j][k]-m[j][i]*a[i][k]
    if a[n-1][n-1]==0:
        print("no unique solution exists")
        return
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for j in range(1,n):
        i = n-j-1
        x[i] = (a[i][n]-S(a,x,i,n))/a[i][i]
    print(x)
    return
f(a,A,n,x,m)