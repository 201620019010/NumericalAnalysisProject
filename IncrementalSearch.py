import math 
from math import *

f = eval("lambda x:"+input("Enter the function: "))
x0 = float(input("Enter x0: "))
delta = float(input("Enter delta: "))
niter = float(input("Enter the maximum number of iterations: "))

print("""
Incremental search results:
""")

fx0 = f(x0)

if float(fx0) == 0.0:
    print(f"{x0} is a root:")
else:
    x1 = x0 + delta
    count = 1
    fx1 = f(x1)

    while(count < niter)  :
        x0 = x1
        fx0 = fx1
        x1 = x0 + delta
        fx1 = f(x1)
        count += 1
        if float(fx0) == 0.0:
            print(f"{x0}is a root")
        if float(fx1) == 0.0:
            print(f"{x1} is a root")
        if float(fx0 * fx1) < 0.0:
            print(f" There is a root between {x0:.10e} and {x1:.10e}")
         #else:
         #print(f"Failed in {niter} interations ")
        