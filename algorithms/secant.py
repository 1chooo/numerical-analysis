import math
def secant(f1,p0,p1,N):
    q0 = f1(p0)
    q1 = f1(p1)
    for i in range (0,20):
        p = p1-q1*(p1-p0)/(q1-q0)
        if abs(p-p1)<1e-10:
            return p
        else:
            i +=1
            p0=p1
            q0 =q1
            p1 = p
            q1 =f(p)
            
f1 = lambda x: math.cos(x)-x
approx1 = secant(f1,0.5,0.785,10)
print(approx1)
