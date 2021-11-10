from gaussian import augmentedMatrixform, progressiveSustitution, regressiveSustitution

A = eval(input("Input A: "))
b = eval(input("Input b: "))
stage = 0

L = []
for i in range(len(A)):
    row = []
    for j in range(len(A)):
        if i != j:
            row.append(0.0)
        else:
            row.append(1.0)
    L.append(row)
U = [[0.0 for i in range(len(A))] for j in range(len(A))]
A = [[float(i) for i in j] for j in A]
U[0] = [i for i in A[0]]

def factorizationLU(A, b, n, stage):
    Ab = augmentedMatrixform(A,b)                      
    for k in range(n-1):
        for i in range(k+1, n):
            L[i][k] = multiplicator = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicator * Ab[k][j])
        stage += 1
        print()
        print(f"Stage {stage}")
        print()
        for i in Ab:
            result = ""
            for j in i[:len(Ab)]:
                result += f"{j:.10e} "
            print(result)
        print()
        print("L:")
        for i in L:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        print()
        print("U:")
        i = Ab[stage]
        U[stage] = i[:len(Ab)]
        for i in U:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        print()
    return Ab

print()
print("LU with simple gaussian:")
print()
print("Results")
print()
print(f"Stage {stage}")
print()
for i in A:
    result = ""
    for j in i:
        result += f"{j} "
    print(result)
Ab = factorizationLU(A,b, len(A),stage)

Lb = augmentedMatrixform(L,b)
z = progressiveSustitution(Lb,len(L))
Uz = augmentedMatrixform(U,z)
x = regressiveSustitution(Uz,len(U))
print()
print("After apply progressive and regressive sustitution")
print()
print("x:")
for i in x:
    print(i)