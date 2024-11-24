def L20(x):
    y = ((x-1.6)*(x-1.9))/((1.3-1.6)*(1.3-1.9))
    return y
def L21(x):
    y = ((x-1.3)*(x-1.9))/((1.6-1.3)*(1.6-1.9))
    return y
def L22(x):
    y = ((x-1.3)*(x-1.6))/((1.9-1.6)*(1.9-1.3))
    return y
def H20(x):
    y = (10*x-12)*L20(x)*L20(x)
    return y
def H21(x):
    y = L21(x)*L21(x)
    return y
def H22(x):
    y = (20-10*x)*L22(x)*L22(x)
    return y
def h20(x):
    y = (x-1.3)*L20(x)*L20(x)
    return y
def h21(x):
    y = (x-1.6)*L21(x)*L21(x)
    return y
def h22(x):
    y = (x-1.9)*L22(x)*L22(x)
    return y
def H5(x):
    y = 0.6200860*H20(x)+0.4554022*H21(x)+0.2818186*H22(x)-0.5220232*h20(x)-0.5698959*h21(x)-0.5811571*h22(x)
    return y
H5(1.5)
