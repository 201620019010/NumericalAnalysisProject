import numpy as np
import math

from numpy.lib.function_base import append


def bisection(parameters):
    #Imprimir ayudas necesarias para el usuario
    #formato de la funcion de entrada para que python la entienda

    resultMatrix=[]
    f=eval("lambda x:"+parameters[0])
    a=eval(parameters[1])
    b=eval(parameters[2])
    ite=eval(parameters[4])
    t=eval(parameters[3])

    print(f(a))
    print(f(b))
    #We first look if the given values belong to the interval where the solution exists.
    '''if not (f(a) * f(b) < 0):
        print('Root for f(x) is not in the given interval')
        exit()
        '''
    # We print a little value table where first values are shown.
    
    resultMatrix.append('--------------------------------------------------------------------------')
    resultMatrix.append('iter \t\t a \t\t b \t\t c \t\t f(c)        ')
    resultMatrix.append('--------------------------------------------------------------------------')
    # We start looping
    for i in range(ite):
        # Bisection's method formula
        c = (a + b) / 2

        # We print some values.
        resultMatrix.append(str(i + 1) + '\t\t% 10.9f\t% 10.9f\t% 10.9f\t% 10.9f\t' % (a, b, c, f(c)))
        
        # We make sure that the experimental value is not greater than the acceptable error
        if np.abs(f(c)) < t:
            resultMatrix.append('--------------------------------------------------------------------------')
            resultMatrix.append('The root is: ' + str(c))
            return(resultMatrix)
        # After the looping process and halving we make sure that the intervals are becoming smaller and smaller.
        if f(a) * f(c) < 0:
            # If the root is closer to the lower limit we switch the a value to a new one in order to get closer.
            b = c
        else:  # The root is between b and c
            #On the other side, if the root is closer to the upper limit we do the exact same thing but with the upper one.
            a = c

    print ("hola")
    return resultMatrix


'''
f="math.log((math.sin(x)**2)+1)-(1/2)"
a=0
b=1
n=100
tol=1e-7

result=bisection(f,a,b,tol,n)

for item in result:
    print(item)
    print("")

'''