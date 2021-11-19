from math import sqrt
import numpy as np
def sor(parameters):
    try:
        A = eval(parameters[0])
        b = eval(parameters[1])
        x0 = eval(parameters[2])
        Tol = eval(parameters[4])
        w = eval(parameters[3])
        Nmax = eval(parameters[5])
    except Exception as e:
        return ["Wrong Parameters Entered"]
    resultMatrix=[]

    resultMatrix.append("Sor")
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
        print(result)
    resultMatrix.append(result)

    resultMatrix.append("C:")

    for i in C:
        resultMatrix.append(str(i))

    val, ne =  np.linalg.eig(T) # T es la matriz
    sr = max(abs(val))
    resultMatrix.append("Spectral Radius: ")
    resultMatrix.append(sr)


    x1 = [0 for i in range(len(A))]
    count = 0
    disp = Tol + 1
    deci = str(int(str(Tol)[4])+2)
    return calculateSor(x0,Tol,Nmax,x1,count,deci,A,b,disp,resultMatrix,w)


def calculateNewSor(A,b,x0,x1,w):
    for i in range(len(A)):
        sum1 = 0
        for j in range(len(A)):
            if j != i:
                sum1 += A[i][j]*x1[j]
        x1[i] = ((1-w)*x0[i])+(w*(b[i] - sum1)/A[i][i])
    return x1

def norm(x1,x0):
    result = 0
    for i, j in zip(x1,x0):
        result += (i-j)**2
    return sqrt(result)

def calculateSor(x0,Tol,Nmax,x1,count,deci,A,b,disp,resultMatrix,w):
    resultMatrix.append("|Iteration| |Error| |Result|")
    while disp > Tol and count < Nmax:
        x1 = calculateNewSor(A,b,x0,x1,w)
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