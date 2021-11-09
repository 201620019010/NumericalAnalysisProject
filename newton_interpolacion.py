import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

def newton(n, x, y):
	j=0
	temp=0
	tabla = np.zeros((n+1,n+1))

	for i in range(n):
		tabla[i][0] = x[i]
		tabla[i][1] = y[i]

	res = polinomeNewton(tabla,n).tolist()
	#print (res)
	for i in range(len(res)):
		res[i].pop(0)
	res.pop()
	return np.array(res).tolist()


def polinomeNewton(tabla,n):
    polinome = "P(X) = " + str(tabla[0][1])
    F = Function('F')
    for j in range(2,n+1):
        for i in range(j-1,n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1])/(tabla[i][0] - tabla[i-j+1][0])
            if(i==j-1):
                polinome += " + " + str(tabla[i][j])
                for i in range(0,i):
                    polinome += "(x - " + str(tabla[i][0]) + ")"
    imprimirTabla(tabla,n)
    F = parse_expr(polinome.replace("P(X) = ","").replace("(","*("))
    print("\nInterpolating Polinome \n" + polinome)

    return tabla

def imprimirTabla(tabla,n):
    print(" n | xi | First | Second | Third | Fourth | Fifth | Nesim |" )
    for i in range(n):
        print(str(i) + "   " + str(tabla[i]).replace(",","    ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
        print("\n")




newton(4,[-1,0,3,4],[15.5,3,8,1])