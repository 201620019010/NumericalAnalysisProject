import numpy as np
from sympy import *
from sympy.core import parameters
from sympy.parsing.sympy_parser import parse_expr
import math

def newtonInterpolation(parameters):
    j=0
    temp=0
    try:
        x=eval(parameters[0])
        y=eval(parameters[1])
    except Exception as e:
        return ["Wrong Parameters Entered"]
    n=np.size(x)
    sizey=np.size(y)

    if sizey!=n:
        return ["Make sure x and y are the same size"]

    if n > len(set(x)):
        return ["There can not be repeated elements in x"]

    tabla = np.zeros((n+1,n+1))

    for i in range(n):
	    tabla[i][0] = x[i]
	    tabla[i][1] = y[i]

    res = polinomeNewton(tabla,n)

    return res


def polinomeNewton(tabla,n):
    responseArray=[]
    polinome = "P(X) = " + str(tabla[0][1])
    F = Function('F')
    for j in range(2,n+1):
        for i in range(j-1,n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1])/(tabla[i][0] - tabla[i-j+1][0])
            if(i==j-1):
                polinome += " + " + str(tabla[i][j])
                for i in range(0,i):
                    polinome += "(x - " + str(tabla[i][0]) + ")"
    imprimirTabla(tabla,n,responseArray)
    F = parse_expr(polinome.replace("P(X) = ","").replace("(","*("))
    responseArray.append("\nInterpolating Polinome \n" + polinome)
    return responseArray

def imprimirTabla(tabla,n,responseArray):
    responseArray.append(" n | xi | First | Second | Third | Fourth | Fifth | Nesim |" )
    for i in range(n):
        responseArray.append(str(i) + "   " + str(tabla[i]).replace(",","    ").replace("["," ").replace("]"," ").replace(" 0 ", " "))




#newtonInterpolation([-1,0,3,4],[15.5,3,8,1])