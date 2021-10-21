import numpy as np
import math


def bisection(function,a,b,iteraciones,tolerancia):
    #Imprimir ayudas necesarias para el usuario
    #formato de la funcion de entrada para que python la entienda

    f=eval(function)
    i=iteraciones
    t=tolerancia

    print(f(a))
    print(f(b))
    #We first look if the given values belong to the interval where the solution exists.
    '''if not (f(a) * f(b) < 0):
        print('Root for f(x) is not in the given interval')
        exit()
        '''
    # We print a little value table where first values are shown.
    print('--------------------------------------------------------------------------')
    print('iter \t\t a \t\t b \t\t c \t\t f(c)        ')
    print('--------------------------------------------------------------------------')

    # We start looping
    for i in range(iteraciones):
        # Bisection's method formula
        c = (a + b) / 2

        # We print some values.
        print(str(i + 1) + '\t\t% 10.9f\t% 10.9f\t% 10.9f\t% 10.9f\t' % (a, b, c, f(c)))

        # We make sure that the experimental value is not greater than the acceptable error
        if np.abs(f(c)) < t:
            print('--------------------------------------------------------------------------')
            print('The root is: ' + str(c))
            exit()
        # After the looping process and halving we make sure that the intervals are becoming smaller and smaller.
        if f(a) * f(c) < 0:
            # If the root is closer to the lower limit we switch the a value to a new one in order to get closer.
            b = c
        else:  # The root is between b and c
            #On the other side, if the root is closer to the upper limit we do the exact same thing but with the upper one.
            a = c

c=0
funct="lambda x: "+"math.log(math.pow(math.sin(c),2)+1)-0.5"
bisection(funct,0,1,100,10E-7)