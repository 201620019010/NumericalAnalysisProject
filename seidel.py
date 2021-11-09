from math import sqrt
import numpy as np
A = eval(input("Enter A: "))
b = eval(input("Enter b: "))
x0 = eval(input("Enter x0: "))
Tol = input("Enter Tol: ")
deci = str(int(str(Tol)[3])+2)
Tol = eval(Tol)
Nmax = eval(input("Enter Nmax: "))

print()
print("Gauss-Seidel")
print()
print("Results:")

H = [[0 if i >= j else -A[i][j] for i in range(len(A))] for j in range(len(A))]
T = [[0 if i < j else A[i][j] for i in range(len(A))] for j in range(len(A))]
T = np.array(T)
C = list((np.linalg.inv(T)).dot(np.array(b)))
T = list((np.linalg.inv(T)).dot(np.array(H)))

print()
print("T:")
for i in T:
    result = ""
    for j in i:
        result += f"{j:.10e} "
    print(result)
print()

print()
print("C:")
for i in C:
    print(i)
print()

val, ne =  np.linalg.eig(T) # T es la matriz
sr = max(abs(val))
print()
print("Spectral Radius: ")
print(sr)
print()

x1 = [0 for i in range(len(A))]
count = 0
disp = Tol + 1

def calculateNewSeidel(x0):
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

while disp > Tol and count < Nmax:
    x1 = calculateNewSeidel(x0)
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

