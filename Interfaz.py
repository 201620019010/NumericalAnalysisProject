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


iteraciones = 100  # Numero de iteraciones
tolerancia = 10E-7  # Error tolerable que se da en las pruebas
a = 0  # Limite inferior
b = 1  # Limite superior

#Miramos primero si el valor cumple con los criterios del metodo
if f(a) * f(b) > 0:
    print('Los valores dados no estan cerca de la raiz')
    exit()

# Imprimimos una tabla que muestra como va progresando el metodo por cada iteracion
print('--------------------------------------------------------------------------')
print('iter \t\t a \t\t b \t\t c \t\t f(c)        ')
print('--------------------------------------------------------------------------')

# Empezamos el metodo
for i in range(iteraciones):
    # Formula de la biseccion
    c = (a + b) / 2

    # Imprimimos algunos valores en la tabla
    print(str(i + 1) + '\t\t% 10.9f\t% 10.9f\t% 10.9f\t% 10.9f\t' % (a, b, c, f(c)))

    # Miramos si la raiz se encuentra y cumple con el error que tenemos pactado desde el principio
    if np.abs(f(c)) < tolerancia:
        print('--------------------------------------------------------------------------')
        print('La raiz aproximada es: ' + str(c))
        exit()
    # Miramos si la raiz se encuentra entre a y c
    if f(a) * f(c) < 0:
        # Cambiamos el limite superior para que el metodo se vaya partiendo a la mitad los intervalos cercanos a la raiz
        b = c
    else:  # La raiz esta entre c y b
        #En este caso es cuando la raiz se aproxima mas al limite inferior y seguimos iterando.
        a = c

