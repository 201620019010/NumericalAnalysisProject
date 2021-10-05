# Fixed point iteration method in Python

import math
import numpy as np

def f(x):
    return np.log(np.sin(x)*np.sin(x)+1)-0.50-x


# We re-write the function in terms of x=g(x)
def g(x):
    return np.log(np.sin(x)*np.sin(x)+1)-0.50


# Fixed point method implementation
def Punto_Fijo(x0, e, N):
    print('\n\n*** Looping with fixed point ***')
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
        print('\nThe root that youre looking for given function is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input values
x0 = input('Initial Value: ')
e = input('Error : ')
N = input('Iterations: ')

# We convert the initial approach and the error into floating numbers in order to not have issues with memory storing and more accuracy
x0 = float(x0)
e = float(e)

# Let's remember that iterations can only be natural number,otherwise it would not make sense
N = int(N)


# Recursive call and test of the given function 
Punto_Fijo(x0, e, N)

