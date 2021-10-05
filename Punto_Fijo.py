# Metodo del punto fijo en Python

import math
import numpy as np

def f(x):
    return np.log(np.sin(x)*np.sin(x)+1)-0.50-x


# Re escribimos f(x)=0 a x = g(x)
def g(x):
    return np.log(np.sin(x)*np.sin(x)+1)-0.50


# Implementacion del metodo de punto fijo
def Punto_Fijo(x0, e, N):
    print('\n\n*** Iterando punto fijo ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f(x1)) > e

    if flag == 1:
        print('\nLa raiz que busca es: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Valores de entrada
x0 = input('Valor inicial: ')
e = input('Error : ')
N = input('Numero de iteraciones: ')

# Convertimos el x0 y el e a flotantes para que el error de redondeo sea menor
x0 = float(x0)
e = float(e)

# Las iteraciones solo pueden ser numeros naturales
N = int(N)


# Comenzando con punto fijo y con su respectiva aproximacion
Punto_Fijo(x0, e, N)

