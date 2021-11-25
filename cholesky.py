import numpy as np
import math

def cholesky(parameters):
   #mlengine=matlab.engine.start_matlab()
    try:
        A=eval(parameters[0])
        b=eval(parameters[1])
    except Exception as e:
        return ["Wrong Parameters Entered"]
    #a=matlab.double(A)
    #c=matlab.double(b)
    resultMatrix=[]

    #answ=mlengine.crout(a,c)
    A=np.array(A)
    b=np.array(b)
    matrixSize=A.shape
    bMatrixSize=b.shape[0]
    if matrixSize != bMatrixSize:
        return ["Matrix size is not the same"]
    L=np.identity(matrixSize[0])
    U=np.identity(matrixSize[0])
    resultMatrix.append("Stage 0 --------------------------")
    resultMatrix.append(np.array2string(np.around(A,decimals=2)))

    for i in range(matrixSize[0]-1):
        resultMatrix.append(("Stage ",i+1,"-------------------"))

        try:
            L[i][i]=math.sqrt(A[i][i]-np.dot(L[i,1:i-1],U[1:i-1,i]))
        except ValueError:
            resultMatrix=[]
            resultMatrix.append("Cant calculate square root of 0 or negative numbers")
            return resultMatrix

        U[i][i]=L[i][i]

        resultMatrix.append("U")  
        resultMatrix.append(np.array2string(np.around(U,decimals=2)))
        
        resultMatrix.append("L")  
        resultMatrix.append(np.array2string(np.around(L,decimals=2)))

        for j in range(i+1,matrixSize[0]):
            if U[i][i]==0:
                return ["There is a cero in U diagonal"]
            L[j][i]=(A[j][i]-np.dot(L[j,1:i-1],U[1:i-1,i]))/U[i][i]


        for j in range(i+1,matrixSize[0]):
            if L[i][i]==0:
                return ["There is a cero in L diagonal"]
            U[i][j]=(A[i][j]-np.dot(L[i,1:i-1],U[1:i-1,j]))/L[i][i]

        
    resultMatrix.append(np.array2string(np.around(A,decimals=2)))


    resultMatrix.append(str("Stage {} -------------").format(matrixSize[0]))
    resultMatrix.append(np.array2string(np.around(A,decimals=2)))
    z=np.linalg.solve(L,b)
    x=np.linalg.solve(U,z)
    resultMatrix.append("Result Matrix-------------")   
    resultMatrix.append(np.array2string(np.around(x,decimals=2))) 
    return resultMatrix

def forwardSubs(A,b):
    size=np.size(A)
    v = [0 for i in range(size)]
    for i in range(size):
        v[i] = (b[i] - v.dotProduct(A[i]))/float(A[i][i])
    return v

def back_substitution(A, b):
    n = np.size(b)
    x = np.zeros_like(b)

    if A[n-1, n-1] == 0:
        raise ValueError

    for i in range(n-1, 0, -1):
        x[i] = A[i, i]/b[i]
        for j in range (i-1, 0, -1):
            A[i, i] += A[j, i]*x[i]

    return x

'''
A="[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]"


b="[1],[1],[1],[1]"

cholesky([A,b])
'''
        