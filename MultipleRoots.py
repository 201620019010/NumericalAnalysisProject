import math
from math import *

def multipleRoots(parameters):
    f = eval("lambda x: "+parameters[0])
    df = eval("lambda x: "+parameters[1])
    df2 = eval("lambda x: "+parameters[2])
    tol = float(parameters[3])
    x0 = float(parameters[4])
    niter = float(parameters[5])

    resultMatrix=[]

    fx = f(x0)
    dfx = df(x0)
    dfx2 = df2(x0)
    cont = 0
    err = tol + 1
   
    resultMatrix.append("Multiple Roots")
    resultMatrix.append("Result Table")
    resultMatrix.append("|i|        xi       |      f(xi)     |        E       |")



    while (err > tol) and (fx != 0) and (dfx != 0) and (dfx2 != 0) and (cont < niter):
        if err == tol + 1:
            resultMatrix.append(f" {cont}  {x0:.10e} {fx:.10e}")
        else:
            if cont < 10:
                resultMatrix.append(f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}")
            else:
                resultMatrix.append(f" {cont} {x0:.10e} {fx:.10e} {err:.10e}")

        x1 = x0 - ((fx*dfx)/((dfx)**2-(fx*dfx2)))
        fx = f(x1)
        dfx = df(x1)
        dfx2 = df2(x1)
        err = abs(x1 - x0)
        x0 = x1
        cont += 1
    if cont < 10:
        resultMatrix.append(f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}")
    else:
        resultMatrix.append(f" {cont} {x0:.10e} {fx:.10e} {err:.10e}")
    if fx == 0:
        resultMatrix.append(f"{x0} is a root")
    elif err < tol:
        resultMatrix.append((f"{x1} is an approximation to a root with a tolerance:", tol))
    elif dfx == 0 or dfx2 == 0:
        resultMatrix.append(f"{x1} is a possible multiple root")
    else:
        resultMatrix.append(f"Failed in {niter} iterations")

    return resultMatrix

'''
f="(math.e**x)-x-1"
df="(math.e**x)-1"
df2="(math.e**x)"
x0=1
n=100
tol=10e-7

result=multipleRoots(f,df,df2,x0,tol,n)

for item in result:
    print(item)
    print("")'''