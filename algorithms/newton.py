import math
def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn)<epsilon:
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            return None
        xn = xn-fxn/Dfxn
    
    return None
    
f = lambda x :math.cos(x)-x
Df = lambda x:-math.sin(x)-1
approx =newton(f,Df,0.5,1e-10,10)
print(approx)
