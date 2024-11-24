import numpy as np

A = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
B = np.array([6,25,-11,15])
C = [0,0,0,0]
T = np.zeros((4, 4))
X = np.transpose([0,0,0,0])
N = 30

for i in range(4):
    for j in range(4):
        T[i][j] = -A[i][j]/A[i][i]
        T[i][i] = 0

for i in range(4):
    C[i] = B[i]/A[i][i]

for i in range(N):
    X = np.matmul(T,X)+C
    print (X)
 