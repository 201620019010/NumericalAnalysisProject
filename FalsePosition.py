import math 
from math import *

ff = eval("lambda x:"+input("Enter the function: "))
xi = float(input("Enter xi: "))
xs = float(input("Enter xs: "))
tol = float(input("Enter tolerance: "))
niter = float(input("Enter the maximum number of iterations: "))


print("""
False position
Results table: 
|i |        a        |        xm       |        b        |      f(Xm)       |        E        |
""")

fxi = f(xi)
fxs = f(xs)

if fxi == 0:
    print(f"{xi} is a root")
elif fxs == 0:
    print(f"{xs}  is a root")
elif (fxi * fxs) < 0:
    xm = (xi) - ((fxi*(xs-xi)) / (fxs-fxi))
    fxm = f(xm)
    count = 1
    error = tol + 1

    while (error > tol) and (fxm != 0) and (count < niter):
        if error == tol + 1:
            print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}")
        else:
            if count < 3:
                print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
            else:
                print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
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
        print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
    else:
        print(f" {count}  {xi:.10e}  {xm:.10e}  {xs:.10e}  {fxm:.10e}  {error:.10e}")
    if fxm == 0:
        print(f"{xm} is a root")
    elif error < tol:
        print(f" {xm} is an approximation to a root with a tolerance:",tol)
    else:
        print(f"Failed in  {niter} iterations")
else:
    print("The interval is inappropriate") 


