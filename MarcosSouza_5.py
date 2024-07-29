import numpy as np
import sympy

def funcao(x):
    
    result= 3*x*((np.sinh((173/200)*x))/np.sinh((173/200)))
    
    return result

def integral(a,b,n,sig,e):
    if n<0:
        print('Inserir valor de N maior que 0.')
    else:
        s0=funcao(a)+funcao(b)
        h=(b-a)/(2*n)
        simpar=0
        spar=0
        
        for j in range(1,n+1):
            simpar+=funcao((a+(2*j-1)*h))
        
        if n>1:
            for k in range(1,n):
                spar+=funcao((a+(2*j*h)))
        else:
            spar=0
            
        i= (h/3)*(s0+(4*simpar)+(2*spar))
        iv=0
        
    while np.absolute(i-iv)>sig and np.absolute(h)>e:
        n=n+n
        h=h/2
        spar=spar+simpar
        for j in range(1,n):
            simpar+=funcao((a+(2*j-1)*h))
        iv= (h/3)*(s0+(4*simpar)+(2*spar))
        
    ifinal = (16*i - iv)/15
      
    return ifinal, n

def integralc(a,b):
    return sympy.integrate(a,b,funcao)
        
            
            
