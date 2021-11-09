import numpy as np 


def crout(A,b):
    print("Stage 0---------------------------")
    print(A)
    matrixSize=A.shape
    L=np.identity(matrixSize[0])
    U=np.identity(matrixSize[0])

    for i in range(matrixSize[0]-1):
        print("Stage ",i+1,"-------------------")
        for j in range(i,matrixSize[0]):
            '''
            sumation=0
            for p in range(j-1):
                sumation=sumation+(L[i][p]*U[p,j])
            
            L[j][i]=A[j][i]-sumation
            '''
            L[j][i]=A[j][i]-np.dot(L[j,1:i-1],U[1:i-1,i])
        print (L)

        for j in range(i+1,matrixSize[0]):
            '''
            sumation=0
            for p in range(j-1):
                sumation=sumation+(L[i][p]*U[p][j])
            
            U[i][j]=(1/L[i][i])*(A[i][j]-sumation)
            '''

            U[i][j]=(A[i,j]-np.dot(L[i,1:i-1],U[1:i-1,j]))/L[i][i]
        print(U)

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

crout(A,b)
        
        


