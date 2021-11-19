import math 
from math import *

#the code needs to show help for the user so that he enters the function in a that python understands
print("If your funcion has a Ln use math.log(value)")
print("If your function has a square root use math.sqrt(value)")
print("If your function has a power of use math.pow(value,power)")

def incrementalSearch(parameters):
    resultMatrix=[]
    try:
        f = eval("lambda x:"+parameters[0])
        x0 = float(parameters[1])
        delta = float(parameters[2])
        niter = float(parameters[3])
    except Exception as e:
        return ["Wrong Parameters Entered"]

    print("""
    Incremental search results:
    """)

    fx0 = f(x0)
    print(fx0)
    if float(fx0) == 0.0:
        print(f"{x0} is a root:")
    else:
        x1 = x0 + delta
        count = 1
        fx1 = f(x1)
        print(niter)
        while(count <= niter)  :
            if float(fx0) == 0.0:
                resultMatrix.append(f"{x0}is a root")
                #print(f"{x0}is a root")
            if float(fx1) == 0.0:
                resultMatrix.append(f"{x1} is a root")
                #print(f"{x1} is a root")
            if float(fx0 * fx1) < 0.0:
                resultMatrix.append(f" There is a root between {x0} and {x1}")
                #print(f" There is a root between {x0} and {x1}")
                
            x0 = x1
            fx0 = fx1
            x1 = x1+ delta
            fx1 = f(x1)
            count += 1

        return resultMatrix

        
        
         #else:
         #print(f"Failed in {niter} interations ")

'''
f="math.log((math.sin(x)**2)+1)-(1/2)"
x0=-3
delta=0.5
n=100
tol=1e-7
print(incrementalSearch(f,x0,delta,tol,n))
'''      