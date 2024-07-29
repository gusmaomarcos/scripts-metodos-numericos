import numpy as np
import matplotlib.pyplot as plt

def modelo1(x1, x2): 
    v=10
    x2f=4
    f=3
    mi=0.53
    kd=0.01
    km=0.12
    Y=0.4
    
    eq1 = ((mi*x1*x2)/(km+x2))-((f/v)+kd)*x1
    
    return eq1

def rungekutta1(x, x10=1.65, x20=0.2, h=0.1): 
    n = int(((x - x10)/h)) 
    y = x10 
    for i in range(1, n+1): 
        k1 = h * modelo1(x10, y) 
        k2 = h * modelo1(x10 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * modelo1(x10 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * modelo1(x10 + h, y + k3) 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
        x10 = x10 + h
    return y

def modelo2(x1, x2): 
    v=10
    x2f=4
    f=3
    mi=0.53
    kd=0.01
    km=0.12
    Y=0.4
    
    eq2 = (f/v)*(x2f-x2)-(1/Y)*(mi*x1*x2/(km+x2))
    
    return eq2

def rungekutta2(x, x10=1.65, x20=0.2, h=0.1): 
    n = int(((x - x20)/h)) 
    y = x20 
    for i in range(1, n+1): 
        k1 = h * modelo2(x20, y) 
        k2 = h * modelo2(x20 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * modelo2(x20 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * modelo2(x20 + h, y + k3) 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
        x20 = x20 + h
    return y

a = list(range(0,31))
b = []
for s in a:
    b.append(rungekutta1(s))
c = []
for t in a:
    c.append(rungekutta2(t))

plt.plot(a,b)
plt.plot(a,c)
plt.title("F = 3")
plt.show()

def modelo1(x1, x2): 
    v=10
    x2f=4
    f=173/300
    mi=0.53
    kd=0.01
    km=0.12
    Y=0.4
    
    eq1 = ((mi*x1*x2)/(km+x2))-((f/v)+kd)*x1
    
    return eq1

def rungekutta1(x, x10=1.65, x20=0.2, h=0.1): 
    n = int(((x - x10)/h)) 
    y = x10 
    for i in range(1, n+1): 
        k1 = h * modelo1(x10, y) 
        k2 = h * modelo1(x10 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * modelo1(x10 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * modelo1(x10 + h, y + k3) 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
        x10 = x10 + h
    return y

def modelo2(x1, x2): 
    v=10
    x2f=4
    f=173/300
    mi=0.53
    kd=0.01
    km=0.12
    Y=0.4
    
    eq2 = (f/v)*(x2f-x2)-(1/Y)*(mi*x1*x2/(km+x2))
    
    return eq2

def rungekutta2(x, x10=1.65, x20=0.2, h=0.1): 
    n = int(((x - x20)/h)) 
    y = x20 
    for i in range(1, n+1): 
        k1 = h * modelo2(x20, y) 
        k2 = h * modelo2(x20 + 0.5 * h, y + 0.5 * k1) 
        k3 = h * modelo2(x20 + 0.5 * h, y + 0.5 * k2) 
        k4 = h * modelo2(x20 + h, y + k3) 
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
        x20 = x20 + h
    return y

a = list(range(0,31))
b = []
for s in a:
    b.append(rungekutta1(s))
c = []
for t in a:
    c.append(rungekutta2(t))

plt.plot(a,b)
plt.plot(a,c)
plt.title("F = DRE3/300")
plt.show()