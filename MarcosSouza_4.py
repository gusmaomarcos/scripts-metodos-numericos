import numpy as np

def decomposicao(a):
    n=len(a)
    for k in range(0, n - 1):
        for i in range(k+1, n):
                fator = a[i,k]/a[k,k]
                a[i,k] = fator
                a[i,k+1:n] = a[i,k+1:n] - fator*a[k,k+1:n]
    
    return a

def sistema(matriz,b):
    a=decomposicao(matriz)
    n=len(a)
    
    for k in range(1,n):
        b[k] = b[k] - np.dot(a[k,0:k],b[0:k])
        b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b


#fatoracao LU da matriz proposta pelo exercicio
am = np.array([[2.,-5.,4.],[1.,3.,-6.],[-1.,-2.,5.]])
print('Matriz inicial A')
print(am)
print()
print('Matriz LU')
print(decomposicao(am))
print()
#resolucao Ax=B para o primeiro sistema de equacoes do exercicio
am = np.array([[2.,-5.,4.],[1.,3.,-6.],[-1.,-2.,5.]])
bm = np.array([[1.],[-10.],[9.]])
print('Ax=B')
print(sistema(am,bm))
print()
#resolucao Ax=B para o segundo sistema de equacoes do exercicio
am = np.array([[2.,-5.,4.],[1.,3.,-6.],[-1.,-2.,5.]])
cm = np.array([[1.],[-173/100.],[9.]])
print('Ax=B para -DRE3/100')
print(sistema(am,cm))
#variavel am chamada mais de uma vez por conta de modificacoes inplace da matriz


