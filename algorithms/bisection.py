def func(x):
    return x*x*x+4*x*x-10

def bisection(a,b):
    if (func(a)*func(b) >= 0) : 
        print ("Bisection Method failed")
        return
    c = a
    while(b-a>=0.005):
        c = (a+b)/2
        if (func(c)==0.0):
            break
        if (func(c)*func(a) < 0):
            b = c 
        else:
            a = c
    print("the value of the root is : ","%.5f"%c)
    
a = 1
b = 2
bisection(a,b)
