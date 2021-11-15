# Fixed point iteration method in Python

import math
import numpy as np



# Fixed point method implementation
def Punto_Fijo(parameters):
    x0 = float(parameters[2])
    tol = float(parameters[3])
    resultMatrix=[]
    N=eval(parameters[4])
    f1=eval("lambda x:"+parameters[0])
    g=eval("lambda x:"+parameters[1])
    resultMatrix.append('\n\n*** Looping with fixed point ***')

    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        resultMatrix.append('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f1(x1)))
        x0 = x1

        step = step + 1

        if step > N:
            flag = 0
            break

        condition = abs(f1(x1)) > tol

    if flag == 1:
        resultMatrix.append('\nThe root that youre looking for given function is: %0.8f' % x1)
    else:
        resultMatrix.append('\nNot Convergent.')

    return resultMatrix


# Input values
'''
f1="math.log((math.sin(x)**2))+1-x"
g="math.log((math.sin(x)**2)+1)-(1/2)"
x0 = 0.5
tol = 1e-7
N = 100


result=Punto_Fijo(f1,g,x0, tol, N)
for item in result:
    print(item)'''

