from gaussian import augmentedMatrixform, progressiveSustitution, regressiveSustitution, partialPivot, swapMarks, rearrange

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
    marks = [i for i in range(n)]                   
    for k in range(n-1):
        L[k][k] = 1
        Ab, higher = partialPivot(Ab, n, k, True)
        if higher != k:
            marks = swapMarks(marks, higher, k)
        mults_aux = {}
        for i in range(k+1, n):
            mults_aux[(i,k)] = multiplicator = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicator * Ab[k][j])
        for i, j in mults_aux:
            Ab[i][j] = mults_aux[(i,j)]
        for i, j in mults_aux:
            L[i][j] = Ab[i][j]
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
        print("P:(marks)")
        result = ""
        for i in marks:
            l = float(i)
            result += "{0:.10e}".format(l)+" "
        print(result)
        print()
    return Ab, marks

print()
print("LU with partial pivot:")
print()
print("Results")
print()
print(f"Stage {stage}")
print()
for i in A:
    result = ""
    for j in i:
        result += f"{j:.10e} "
    print(result)
Ab, marks = factorizationLU(A,b, len(A), stage)

b = rearrange(b, marks)
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