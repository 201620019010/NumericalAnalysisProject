import math
from math import *


f = eval("lambda x:"+input("Enter the function: "))
df = eval("lambda x:"+input("Enter the derivative of the function: "))
tol = float(input("Enter tolerance: "))
x0 = float(input("Enter x0: "))
niter = float(input("Enter the maximum number of iterations: "))

print("""
Newton
Results table: 
|i|        xi       |     f(xi)      |        E       | 
""")

fx = f(x0)
dfx = df(x0)

count = 0
err = tol + 1

while (err > tol) and (fx != 0) and (dfx != 0) and (count < niter):
    if err == tol + 1:
        print(f" {count}  {x0:.10e} {fx:.10e}")
    else:
        if count < 10:
            print(f" {count}  {x0:.10e} {fx:.10e} {err:.10e}")
        else:
            print(f" {count} {x0:.10e} {fx:.10e} {err:.10e}")
    x1 = x0 - (fx/dfx)
    fx = f(x1)
    dfx = df(x1)
    err = abs(x1 - x0)
    x0 = x1
    count += 1
if count < 10:
    print(f" {count}  {x0:.10e} {fx:.10e} {err:.10e}")
else:
    print(f" {count} {x0:.10e} {fx:.10e} {err:.10e}")
if fx == 0:
    print(f"{x0} is a root")
elif err < tol:
    print(f"{x1} es an approximation to a root with a tolerance:", tol)
elif dfx == 0:
    print(f"{x1} is a possible multiple root")
else:
    print(f"Failed in {niter } iterations")