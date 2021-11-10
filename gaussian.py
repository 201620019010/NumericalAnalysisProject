import sys
def elimination(A, b, n):
    Ab = augmentedMatrixform(A,b)
    stage = 0
    print("Results")
    print()
    print(f"Stage {stage}")
    print()
    stage += 1
    for i in A:
        result = ""
        for j in i:
            result += f"{j:.10e} "
        print(result)
    for k in range(n-1):
        for i in range(k+1, n):
            multiplicator = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= (multiplicator * Ab[k][j])
        print()
        print(f"Stage {stage}")
        print()
        for i in Ab:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        stage += 1
    return Ab

def augmentedMatrixform(A,b):
    for a, b in zip(A, b):
        a.append(b)
    return A

def progressiveSustitution(Lb, n):
    x = [Lb[0][n] / Lb[0][0]]
    while len(x) < n:
        r = 0
        for i in range(len(x)):
            r += Lb[len(x)][i]*x[i]
        r = (Lb[len(x)][n] - r)/Lb[len(x)][len(x)]
        x.append(r)
    return x

def regressiveSustitution(Ab, n):
    x = [0 for i in range(n)]
    x[n-1] = Ab[n-1][n] / Ab[n-1][n-1]
    for i in range(n-1, -1, -1):
        summation = 0
        for p in range(i+1, n):
            summation += Ab[i][p] * x[p]
        x[i] = (Ab[i][n] -  summation)/Ab[i][i]
    return x

def swaprows (Ab, longestRow, k):
    auxRow = Ab[k]
    Ab[k] = Ab[longestRow]
    Ab[longestRow] = auxRow
    return Ab

def columnsSwap(Ab, longestColumn, k):
    columAux = [Ab[i][k] for i in range(len(Ab))]
    for i in range(len(Ab)):
        Ab[i][k] = Ab[i][longestColumn]
    for i in range(len(Ab)):
        Ab[i][longestColumnF] = columAux[i]
    return Ab

def partialPivot(Ab, n, k, lu=False):
    higher = abs(Ab[k][k])
    highRow = k
    for s in range(k+1, n):
        if abs(Ab[s][k]) > higher:
            higher = abs(Ab[s][k])
            highRow = s
    if higher == 0:
        print("The system does not have a unique solution")
        sys.exit()
    else:
        if highRow != k:
            Ab = swapRows(Ab, highRow, k)
        if lu:
            return Ab, highRow
        return Ab

def swapMarks(marks, columnHigher, k):
    markAux = marks[k]
    marks[k] = marks[columnHigher]
    marks[columnHigher] = markAux
    return marks


def totalPivot(Ab, n, k, marks):
    higher = 0
    highRow = k
    columnHigher = k
    for r in range(k, n):
        for s in range(k, n):
            if abs(Ab[r][s]) > higher:
                higher = abs(Ab[r][s])
                highRow = r
                columnHigher = s
    if higher == 0:
        print("The system does not have a unique solution")
        sys.exit()
    else:
        if highRow != k:
            Ab = swapRows(Ab, highRow, k)
        if columnHigher != k:
            Ab = swapColumns(Ab, columnHigher, k)
            marks = swapMarks(marks, columnHigher, k)
        return Ab, marks

def gaussianEliminationWithPivot(A, b, n, pivot="parcial"):
    Ab = augmentedmatrixform(A, b)
    if pivot == "partial" or pivot == "partialLU":
        if pivot == "parcial":
            stage = 0
            print("Resultados")
            print()
            print(f"Stage {stage}")
            print()
            for i in A:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                print(result)
            stage += 1
        else:
            stage = None
        pivot = partialPivot
        for k in range(n-1):
            Ab = pivot(Ab, n, k)
            for i in range(k + 1, n):
                multiplicator = Ab[i][k] / Ab[k][k]
                for j in range(k, n+1):
                    Ab[i][j] -= multiplicator * Ab[k][j]
            if stage:
                print()
                print(f"Stage {stage}")
                print()
                for i in Ab:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    print(result)
                stage += 1
        return Ab
    else:
        stage = 0
        print("Results")
        print()
        print(f"Stage {stage}")
        print()
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            print(result)
        stage += 1
        pivot = totalPivot
        marks = [i for i in range(n)]
        for k in range(n-1):
            Ab, marks = pivot(Ab, n, k, marks)
            for i in range(k + 1, n):
                multiplicator = Ab[i][k] / Ab[k][k]
                for j in range(k, n+1):
                    Ab[i][j] -= multiplicator * Ab[k][j]
            print()
            print(f"Stage {stage}")
            print()
            for i in Ab:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                print(result)
            stage += 1
            
        return Ab, marks

def rearrange(x, marks):
    x_aux = [i for i in x]
    order = [i for i in range(len(x))]
    for i, j in zip(marks,order):
        x[i] = x_aux[j]
    return x

def printMatriz(m):
    for i in m:
        print(i)