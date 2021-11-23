# Trazador (spline) lineal, grado 1
import numpy as np
import sympy as sp

def linealTrace(xi,fi):
    n = len(xi)
    x = sp.Symbol('x')
    polinome = []
    segment=1
    while not(segment>=n):
        m =(fi[segment]-fi[segment-1])/(xi[segment]-xi[segment-1])
        start = fi[segment-1]-m*xi[segment-1]
        psegment = start + m*x
        polinome.append(psegment)
        segment = segment + 1
    return(polinome)
def spline1(parameters):
    # PROGRAM
    # Start , Test Data
    try:
        xi = eval(parameters[0])
        fi = eval(parameters[1])
    except Exception as e:
        return ["Wrong Parameters Entered"]

    
    responseArray=[]
    resolucion = 10 # between each pair of points

    # PRocedure
    n = len(xi)
    # Obtains the polinome by segments
    n=np.size(xi)
    sizey=np.size(fi)
    if sizey!=n:
        return ["Make sure x and y are the same size"]

    if n > len(set(xi)):
        return ["There can not be repeated elements in x"]

    for i in range(n-1):
        if xi[i]>xi[i+1]:
            return ["Error x are not in ascending order"]


    polinome = linealTrace(xi,fi)

    # OUT
    responseArray.append('Polinome by Segments: ')
    for segment in range(1,n,1):
        responseArray.append(' x = ['+str(xi[segment-1])
            +','+str(xi[segment])+']')
        
        responseArray.append(str(polinome[segment-1]))
    return responseArray