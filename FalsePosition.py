import math 
from math import *

def falsePosition(parameters):
    try:
        f= eval("lambda x:"+parameters[0])
        xi = float(parameters[1])
        xs = float(parameters[2])
        tol = float(parameters[3])
        niter = float(parameters[4])
    except ValueError:
        return ["Wrong Parameters Entered"]
    resultMatrix=[]


    resultMatrix.append("False position")
    resultMatrix.append("Results table: ")
    resultMatrix.append("|i |        a        |        xm       |        b        |      f(Xm)       |        E        |")

    fxi = f(xi)
    fxs = f(xs)

    if fxi == 0:
        resultMatrix.append(f"{xi} is a root")
    elif fxs == 0:
        resultMatrix.append(f"{xs}  is a root")
    elif (fxi * fxs) < 0:
        xm = (xi) - ((fxi*(xs-xi)) / (fxs-fxi))
        fxm = f(xm)
        count = 1
        error = tol + 1

        while (error > tol) and (fxm != 0) and (count < niter):
            if error == tol + 1:
                resultMatrix.append(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}")
            else:
                if count < 3:
                    resultMatrix.append(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
                else:
                    resultMatrix.append(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
            if (fxi * fxm) < 0:
                xs = xm
                fxs = fxm
            else:
                xi = xm
                fxi = fxm
            xaux = xm
            xm = (xi) - ((fxi*(xs-xi)) / (fxs-fxi))
            fxm = f(xm)
            error = abs(xm - xaux)
            count += 1
        if count < 3:
            resultMatrix.append(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
        else:
            resultMatrix.append(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
        if fxm == 0:
            resultMatrix.append(f"{xm} is a root")
        elif error < tol:
            resultMatrix.append((f" {xm} is an approximation to a root with a tolerance:",tol))
        else:
            resultMatrix.append(f"Failed in  {niter} iterations")
    else:
        resultMatrix.append("The interval is inappropriate")

    return resultMatrix

'''
f="math.log((math.sin(x)**2)+1)-(1/2)"
a=0
b=1
n=100
tol=1e-7
result=falsePosition(f,a,b,tol,n)

for item in result:
    print(item)
    '''