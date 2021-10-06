import math
from math import *

f = eval("lambda x: "+input("Enter function: "))
df = eval("lambda x: "+input("Enter the derivative of the function: "))
df2 = eval("lambda x: "+input("Enter the second derivative of the function: "))
tol = float(input("Enter tolerance: "))
x0 = float(input("Enter x0: "))
niter = float(input("Enter the maximum number of iterations:"))

fx = f(x0)
dfx = df(x0)
dfx2 = df2(x0)
cont = 0
err = tol + 1
print("""
Multiple Roots
Result Table 
|i|        xi       |      f(xi)     |        E       |
""")


while (err > tol) and (fx != 0) and (dfx != 0) and (dfx2 != 0) and (cont < niter):
    if err == tol + 1:
        print(f" {cont}  {x0:.10e} {fx:.10e}")
    else:
        if cont < 10:
            print(f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}")
        else:
            print(f" {cont} {x0:.10e} {fx:.10e} {err:.10e}")
    x1 = x0 - ((fx*dfx)/((dfx)**2-(fx*dfx2)))
    fx = f(x1)
    dfx = df(x1)
    dfx2 = df2(x1)
    err = abs(x1 - x0)
    x0 = x1
    cont += 1
if cont < 10:
    print(f" {cont}  {x0:.10e} {fx:.10e} {err:.10e}")
else:
    print(f" {cont} {x0:.10e} {fx:.10e} {err:.10e}")
if fx == 0:
    print(f"{x0} is a root")
elif err < tol:
    print(f"{x1} is an approximation to a root with a tolerance:", tol)
elif dfx == 0 or dfx2 == 0:
    print(f"{x1} is a possible multiple root")
else:
    print(f"Failed in {niter} iterations")