import numpy as np 

def doolittle(A,b):
    print("Stage 0---------------------------")
    print(A)
    matrixSize=A.shape
    L=np.identity(matrixSize[0])
    U=np.identity(matrixSize[0])

    for i in range(matrixSize[0]-1):
        print("Stage ",i+1,"-------------------")
        for j in range(i,matrixSize[0]):
            U[i,j]=A[i,j]-np.dot(L[i,1:i-1],U[1:i-1,j])
        print(U)

        for j in range(i+1,matrixSize[0]):
            L[j,i]=(A[j][i]-np.dot(L[j,1:i-1],U[1:i-1,i]))/U[i][i]

        print(L)

A=np.array([
    [4,-1,0,3],
    [1,15.5,3,8],
    [0,-1.3,-4,1.1],
    [14,5,-2,30]
])

b=np.array([
    [1],
    [1],
    [1],
    [1]
])

doolittle(A,b)
