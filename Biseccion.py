import numpy as np


def bisection(f,a,b,N):
    '''.
    Approximate solution of f(x)=0 on interval [a,b] by bisection method
    Parameters
    Spanish:Solucion aproximada de la funcion f(x)=0 en el intervalo [a,b] por el metodo de la biseccion
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
        Spanish:La funcion donde queremos encontrar una solucion a f(x)=0

    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
        Spanish:Intervalo dado, recordemos que si f(a)*f(b)>=0 no se garantiza una solucion
    N : (positive) integer
        The number of iterations to implement.
        Iteraciones a implementar

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.


    '''

    # Define the function whose roots are required


def f(x):
    # return ln(sin^2(x)+1)-0.5
    return np.log(np.sin(x)*np.sin(x)+1)-(0.5)


iteraciones = 100  # Number of iterations
tolerancia = 10E-7  # Acceptable error given in testing costraints.
a = 0  # Lower Limit
b = 1  # Upper Limit

#We first look if the given values belong to the interval where the solution exists.
if f(a) * f(b) > 0:
    print('Root for f(x) is not in the given interval')
    exit()

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
    if np.abs(f(c)) < tolerancia:
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

