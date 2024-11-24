i=1
p0=1.5
tol=0.001
def f(x):
    y = x**3+4*x*x-10
    return y
def g(x):
    g = (1/2)*(10-x**3)**(1/2)
    return g
while i<10000:
    p = g(p0)
    E = abs(p-p0)
    if E<tol:
        break
    else:
        i+=1
        p0=p
print(p0)
