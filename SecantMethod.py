import math
from math import *

def secantMethod(parameters):
    f = eval("lambda x:"+parameters[0])
    x0 = float(parameters[1])
    x1 = float(parameters[2])
    tol = float(parameters[3])
    niter = float(parameters[4])
    resultMatrix=[]


    resultMatrix.append("Secant")
    resultMatrix.append("Results table:")
    resultMatrix.append("|i|        xi       |      f(xi)     |        E       |")
    

    fx0 = f(x0)

    if fx0 == 0:
        resultMatrix.append(f"{x0} is a root: ")

    else:
        fx1 = f(x1)
        cont = 0
        err = tol + 1
        err_aux = tol + 1
        den = fx1 - fx0
        while err_aux > tol and fx1 != 0 and den != 0 and cont < niter:
            if err_aux == tol + 1:
                resultMatrix.append(f" {cont}  {x0:.10e} {fx0:.10e}")
            else:
                if cont < 10:
                    resultMatrix.append(f" {cont}  {x0:.10e} {fx0:.10e} {err_aux:.10e}")

                else:
                    resultMatrix.append(f" {cont} {x0:.10e} {fx0:.10e} {err_aux:.10e}")
            err_aux = err
            x2 = x1 - fx1 * (x1 - x0)/den
            err = abs(x2 - x1)
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f(x1)
            den = fx1 - fx0
            cont += 1
        if cont < 10:
            resultMatrix.append(f" {cont}  {x0:.10e} {fx0:.10e} {err_aux:.10e}")
        else:
            resultMatrix.append(f" {cont} {x0:.10e} {fx0:.10e} {err_aux:.10e}")
        if fx1 == 0:
            resultMatrix.append(f"{x1} is a root ")
        elif err < tol:
            resultMatrix.append(f"{x1} is an approximation to a root with a tolerance: ", tol)
        elif den == 0:
            resultMatrix.append("there is a posible multiple root")
        else:
            resultMatrix.append(f"Failed in {niter } iterations: ")
    return resultMatrix


'''
f="math.log((math.sin(x)**2)+1)-(1/2)"

x0=0
x1=1
n=100
tol=1e-7

result=secantMethod(f,x0,x1,tol,n)

for item in result:
    print(item)
    print("")

    '''

