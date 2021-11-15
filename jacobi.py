from math import sqrt
import numpy as np
from numpy.lib.function_base import append

def jacobi(parameters):
    A = eval(parameters[0])
    b = eval(parameters[1])
    x0 = eval(parameters[2])
    Tol = eval(parameters[3])
    deci = str(int(str(Tol)[3])+2)
    Nmax = eval(parameters[4])
    resultMatrix=[]

    resultMatrix.append("Jacobi")
    resultMatrix.append("Results:")


    C = []
    T = [[0 for i in range(len(A))] for j in range(len(A))]
    for i in range(len(A)):
        coef = 0
        C.append((1/A[i][i])*b[i])
        coef = -(1/A[i][i])
        for j in range(len(A)):
            if i != j:
                T[i][j] = A[i][j]*coef

    resultMatrix.append("T:")
    for i in T:
        result = ""
        for j in i:
            result += f"{j} "
    resultMatrix.append(result)

    resultMatrix.append("C:")
    for i in C:
        resultMatrix.append(str(i))

    val, ne =  np.linalg.eig(T) # T is the matrix
    sr = max(abs(val))
    resultMatrix.append("Spectral Radius: ")
    resultMatrix.append(sr)
  
    x1 = [0 for i in range(len(A))]
    count = 0
    disp = Tol + 1
    return calculateJacobi(x0,Tol,Nmax,x1,count,deci,A,b,disp,resultMatrix)

def calculateNewJacobi(A,b,x0,x1):
    for i in range(len(A)):
        sum1 = 0
        for j in range(len(A)):
            if j != i:
                sum1 += A[i][j]*x0[j]
        x1[i] = (b[i] - sum1)/A[i][i]
    return x1

def norm(x1,x0):
    result = 0
    for i, j in zip(x1,x0):
        result += (i-j)**2
    return sqrt(result)

def calculateJacobi(x0,Tol,Nmax,x1,count,deci,A,b,disp,resultMatrix):
    resultMatrix.append("|Iteration| |Error| |Result|")
    while disp > Tol and count < Nmax:
        x1 = calculateNewJacobi(A,b,x0,x1)
        result = [f"{i}" for i in x0]
        if count <= 9:
            ite = f"0{count}"
        else:
            ite = count
        
        resultMatrix.append(f"|{ite}|        |{disp:.{deci}f}|  |{result}|")
        count += 1
        disp = norm(x1,x0)
        x0 = [i for i in x1]
    if disp < Tol:
        if count <= 9:
            ite = f"0{count}"
        else:
            ite = count
        result = [f"{i:.10e}" for i in x0]
        resultMatrix.append(f"|{ite}|        |{disp:.{deci}f}|  |{result}|")
        resultMatrix.append("x:")
       
        for i in x0:
            resultMatrix.append(str(i))
    else:
        resultMatrix.append(f"Failed in {Nmax} Iterations")

    return resultMatrix

'''
A="[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]"
b="[1,1,1,1]"
x0="[0,0,0,0]"
tol="10e-7"
n="100"

jacobi([A,b,x0,tol,n])
'''