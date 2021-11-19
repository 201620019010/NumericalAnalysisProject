import numpy as np
import math

def cholesky(parameters):
   #mlengine=matlab.engine.start_matlab()
    try:
        A=eval(parameters[0])
        b=eval(parameters[1])
    except ValueError:
        return ["Wrong Parameters Entered"]
    #a=matlab.double(A)
    #c=matlab.double(b)
    resultMatrix=[]

    #answ=mlengine.crout(a,c)
    A=np.array(A)
    b=np.array(b)
    matrixSize=A.shape
    L=np.identity(matrixSize[0])
    U=np.identity(matrixSize[0])
    resultMatrix.append("Stage 0 --------------------------")
    for x in A:
        resultMatrix.append(np.array2string(x))

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
        for x in U:
            resultMatrix.append(np.array2string(x)) 
        
        resultMatrix.append("L")  
        for x in L:
            resultMatrix.append(np.array2string(x)) 

        for j in range(i+1,matrixSize[0]):
            L[j][i]=(A[j][i]-np.dot(L[j,1:i-1],U[1:i-1,i]))/U[i][i]


        for j in range(i+1,matrixSize[0]):
            U[i][j]=(A[i][j]-np.dot(L[i,1:i-1],U[1:i-1,j]))/L[i][i]

        
    for x in A:
        resultMatrix.append(np.array2string(x))
        
    return resultMatrix

'''
A="[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]"


b="[1],[1],[1],[1]"

cholesky([A,b])
'''
        