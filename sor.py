from math import sqrt
import numpy as np
A = eval(input("Enter A: "))
b = eval(input("Enter b: "))
x0 = eval(input("Enter x0: "))
Tol = eval(input("Enter Tol: "))
w = eval(input("Enter w: "))
Nmax = eval(input("Enter Nmax: "))

print()
print("SOR(relaxation)")
print()
print("Results:")
print()
C = []
T = [[0 for i in range(len(A))] for j in range(len(A))]
for i in range(len(A)):
    coef = 0
    C.append((1/A[i][i])*b[i])
    coef = -(1/A[i][i])
    for j in range(len(A)):
        if i != j:
            T[i][j] = A[i][j]*coef

print()
print("T:")
for i in T:
    result = ""
    for j in i:
        result += f"{j} "
    print(result)

print()
print("C:")
for i in C:
    print(i)

val, ne =  np.linalg.eig(T) # T es la matriz
sr = max(abs(val))
print()
print("Spectral Radius: ")
print(sr)


x1 = [0 for i in range(len(A))]
count = 0
disp = Tol + 1
deci = str(int(str(Tol)[4])+2)

def calculateNewSor(x0):
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

while disp > Tol and count < Nmax:
    x1 = calculateNewSor(x0)
    result = [f"{i:.10e}" for i in x0]
    if count <= 9:
        ite = f"0{count}"
    else:
        ite = count
    print(f"{ite} {disp:.{deci}f} {result}")
    disp = (norm(x1,x0))
    x0 = [i for i in x1]    
    count += 1
    
if disp < Tol:
    if count <= 9:
        ite = f"0{count}"
    else:
        ite = count
    result = [f"{i:.10e}" for i in x0]
    print(f"{ite} {disp:.{deci}f} {result}")
    print()
    print("x:")
    for i in x0:
        print(i)
else:
    print(f"Failed in {Nmax} iterations")