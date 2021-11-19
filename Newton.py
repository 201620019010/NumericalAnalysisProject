import math
from math import *

def newton(parameters):
    try:
        f = eval("lambda x:"+parameters[0])
        df = eval("lambda x:"+parameters[1])
        tol = float(parameters[2])
        x0 = float(parameters[3])
        niter = float(parameters[4])
    except ValueError:
        return ["Wrong Parameters Entered"]
    resultMatrix=[]


    resultMatrix.append("Newton")
    resultMatrix.append("Results table: ")
    resultMatrix.append("|i|        xi       |     f(xi)      |        E       |")

    fx = f(x0)
    dfx = df(x0)

    count = 0
    err = tol + 1

    while (err > tol) and (fx != 0) and (dfx != 0) and (count < niter):
        if err == tol + 1:
            resultMatrix.append(f" {count}        {x0}       |  {fx:.10e}     |      null      |")
        else:
            if count < 10:
                resultMatrix.append(f" {count}        {x0}       |     {fx:.10e}       |     {err:.10e}")
            else:
                resultMatrix.append(f" {count}        {x0}       |     {fx:.10e}       |     {err:.10e}")
        x1 = x0 - (fx/dfx)
        fx = f(x1)
        dfx = df(x1)
        err = abs(x1 - x0)
        x0 = x1
        count += 1
    if count < 10:
        resultMatrix.append(f" {count}  {x0}       |     {fx:.10e}       |     {err:.10e}")
    else:
        resultMatrix.append(f" {count}  {x0}       |     {fx:.10e}       |     {err:.10e}")
    if fx == 0:
        resultMatrix.append(f"{x0} is a root")
    elif err < tol:
        resultMatrix.append((f"{x1} is an approximation to a root with a tolerance:", tol))
    elif dfx == 0:
        resultMatrix.append(f"{x1} is a possible multiple root")
    else:
        resultMatrix.append(f"Failed in {niter } iterations")

    return resultMatrix

'''
f="math.log((math.sin(x)**2)+1)-(1/2)"
df="2*(((math.sin(x)**2)+1)**-1)*math.sin(x)*math.cos(x)"

x0=0.5
n=100
tol=1e-7

result=newton(f,df,x0,tol,n)

for item in result:
    print(item)
    print("")'''