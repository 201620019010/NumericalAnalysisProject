from math import sqrt
import numpy as np

def seidel(parameters):
    A = eval(parameters[0])
    b = eval(parameters[1])
    x0 = eval(parameters[2])
    Tol = eval(parameters[3])
    deci = str(int(str(Tol)[3])+2)
    Nmax = eval(parameters[4])
    resultMatrix=[]

    resultMatrix.append("Seidel")
    resultMatrix.append("Results:")

    H = [[0 if i >= j else -A[i][j] for i in range(len(A))] for j in range(len(A))]
    T = [[0 if i < j else A[i][j] for i in range(len(A))] for j in range(len(A))]
    T = np.array(T)
    C = list((np.linalg.inv(T)).dot(np.array(b)))
    T = list((np.linalg.inv(T)).dot(np.array(H)))


    resultMatrix.append("T:")
    for i in T:
        result = ""
        for j in i:
            result += f"{j:.10e} "
    resultMatrix.append(result)
    

    resultMatrix.append("C:")
    for i in C:
        print(i)
    resultMatrix.append(C)

    val, ne =  np.linalg.eig(T) # T es la matriz
    sr = max(abs(val))

    resultMatrix.append("Spectral Radius: ")
    resultMatrix.append(sr)

    x1 = [0 for i in range(len(A))]
    count = 0
    disp = Tol + 1

    return calculateSeidel(x0,Tol,Nmax,x1,count,deci,A,b,disp,resultMatrix)

def calculateNewSeidel(A,b,x0,x1):
    for i in range(len(A)):
        x1[i] = x0[i]
    for i in range(len(A)):
        sum1 = 0
        for j in range(len(A)):
            if j != i:
                sum1 += A[i][j]*x1[j]
        x1[i] = (b[i] - sum1)/A[i][i]
    return x1

def norm(x1,x0):
    result = 0
    for i, j in zip(x1,x0):
        result += (i-j)**2
    return sqrt(result)

def calculateSeidel(x0,Tol,Nmax,x1,count,deci,A,b,disp,resultMatrix):
    resultMatrix.append("|Iteration| |Error| |Result|")
    while disp > Tol and count < Nmax:
        x1 = calculateNewSeidel(A,b,x0,x1)
        result = [f"{i:.10e}" for i in x0]
        if count <= 9:
            ite = f"0{count}"
        else:
            ite = count
        resultMatrix.append(f"|{ite}|        |{disp:.{deci}f}|  |{result}|")
        disp = (norm(x1,x0))
        x0 = [i for i in x1]   
        count += 1
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

