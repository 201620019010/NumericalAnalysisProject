import math 
from math import *

#the code needs to show help for the user so that he enters the function in a that python understands
print("If your funcion has a Ln use math.log(value)")
print("If your function has a square root use math.sqrt(value)")
print("If your function has a power of use math.pow(value,power)")


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

    while(count <= niter)  :

        if float(fx0) == 0.0:
            print(f"{x0}is a root")
        if float(fx1) == 0.0:
            print(f"{x1} is a root")
        if float(fx0 * fx1) < 0.0:
            print(f" There is a root between {x0-delta} and {x1-delta}")
            
        x0 = x1
        fx0 = fx1
        x1 = x1+ delta
        fx1 = f(x1)
        count += 1

        
        
         #else:
         #print(f"Failed in {niter} interations ")
        