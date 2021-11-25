import math 
from math import *

def falsePosition(parameters):
    try:
        f= eval("lambda x:"+parameters[0])
        xi = float(parameters[1])
        xs = float(parameters[2])
        tol = float(parameters[3])
        niter = float(parameters[4])
    except Exception as e:
        return ["Wrong Parameters Entered"]

    if tol<0:
        return ["Tolerance can not be negative"]
    if niter<0:
        return ["Iterations can not be negative"]
    if (xi>xs):
        return ["a must be less than b"]

    try:
        result=f(xi)
    except Exception:
        return ["a must exist in the function , try a different a value "]

    try:
        result2=f(xs)
    except Exception:
        return ["b must exist in the function , try a different b value "]

    resultMatrix=[]


    resultMatrix.append("False position")
    resultMatrix.append("Results table: ")
    resultMatrix.append("|i   |    a     |        xm        |      b         |    f(Xm)        |        E         |")

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
                resultMatrix.append(f" {count}   {xi:.5f}     {xm:.5f}     {xs:.5f}       {fxm:.5f}")
            else:
                if count < 3:
                    resultMatrix.append(f" {count}   {xi:.5f}     {xm:.5f}     {xs:.5f}       {fxm:.5f}       {error:.5e}")
                else:
                    resultMatrix.append(f" {count}   {xi:.5f}     {xm:.5f}     {xs:.5f}       {fxm:.5f}       {error:.5e}")
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
            resultMatrix.append(f" {count}   {xi:.5f}     {xm:.5f}     {xs:.5f}       {fxm:.5f}       {error:.5e}")
        else:
            resultMatrix.append(f" {count}   {xi:.5f}     {xm:.5f}     {xs:.5f}       {fxm:.5f}       {error:.5e}")
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