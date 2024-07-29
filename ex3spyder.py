import numpy as np
import matplotlib.pyplot as plt

#funcao para o reator CSTR
def func(x):
    f = x + 0.1 - ((0.05*np.exp((20*x)/(1+x))/(1+0.1*np.exp((20*x)/(1+x)))))
    return f

#plot inicial do grafico para auxiliar na escolha dos intervalos, marcar DRE3/1000
# e o valor de f(DRE3/1000)
m = np.linspace(-.2,.5,100)
n = func(m)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.text(0.03, -0.06, "DRE3/1000", fontsize=10, color="red")
ax.text(0.03, -0.10, 'f(DRE3/1000 = ) ' + str(func(0.173)), fontsize=10, color="red")
plt.plot(0.173,func(0.173),color='red',marker='X')
plt.plot(m,n,color='blue')
plt.show()

#algoritmo para o metodo de wegstein e plot da raiz encontrada em grafico
def cstr(a,b,e,sig,km):
    inia = a
    inib = b
    fa = func(a)
    fb = func(b)
    k = 0
    delt = np.absolute(b-a)
   
    if fa*fb > 0:
        print('Inserir novo intervalo.')
    else:
        lambd = fa/(fa-fb)
        x0 = inia + lambd*(inib-inia)
        y = func(x0)    
            
        
        while k<km and delt > e or np.absolute(y) > sig:
            lambd = fa/(fa-fb)
            x0 = a + lambd*(b-a)
            y = func(x0)
            
            if y*fa>0:
                fa = y
                a = x0
            else:
                fb = y
                b = x0
                
            #alteracao do algoritmo para casos onde a condicao delt > e
            # e sempre verdadeira
            if y<1e-11:
                e = e*10
            #
            
            delt = np.absolute(b-a)
            k = k+1
            
            
            #o paragrafo seguinte foi utilizado para se investigar a cada loop
            #quais condicoes eram alcancadas
            '''if delt > e:
                print('condicao delt alcancada')
            if np.absolute(y) > sig:
                print('condicao sig alcancada')'''
            
        #plot final do grafico de acordo com os parametros fornecidos, indicando a 
        #raiz encontrada.
        m = np.linspace(-.2,.5,100)
        n = func(m)
        fig = plt.figure()
        
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.text(0.05, 0.1, 'x0 = ' + str(x0), fontsize=10, color="black")
        ax.text(0.05, 0.089, 'f(x0) = ' + str(y), fontsize=10, color="black")
        ax.text(0.05, 0.077, 'k = ' + str(k), fontsize=10, color="black")
        ax.text(0.05, 0.065, 'a = ' + str(inia), fontsize=10, color="black")
        ax.text(0.05, 0.053, 'b = ' + str(inib), fontsize=10, color="black")
        
        plt.plot(m,n,color='blue')
        plt.plot(x0,y,color='black',marker='X')
        plt.show()
        
        print ('x0 = ' + str(x0) + 
               '\nf(x0) = ' + str(y) +
               '\nIntervalo: (' + str(inia)+', ' +str(inib)+ ')'
               '\nk = ' + str(k))


