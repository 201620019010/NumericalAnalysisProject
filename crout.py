import numpy as np
from numpy.core.fromnumeric import size 
#import matlab.engine 
#import matlab


def crout(parameters):
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
        #print("Stage ",i+1,"-------------------")
        resultMatrix.append(("Stage ",i+1,"-------------------"))

        dotL=np.zeros(i)
        dotU=np.zeros(i)
        for j in range(i,matrixSize[0]):
            if L[i][i]==0:
                return ["There is a cero in L diagonal"]
            '''
            sumation=0
            for p in range(k-1):
                sumation=sumation+(L[i][p]*U[p][k])
            
            L[i][k]=A[i][k]-sumation
            
            '''
            dotL=L[j,1:i-1]
            dotU=U[1:i-1,i]
       
            dotLU=np.dot(dotL,dotU)
            L[j][i]=A[j][i]-dotLU
        
        resultMatrix.append("L")  
        resultMatrix.append(np.array2string(np.around(L,decimals=2)))

        for j in range(i+1,matrixSize[0]):
            '''
            sumation=0
            for p in range(k-1):
                sumation=sumation+(L[k][p]*U[p][i])
            
            U[i][j]=(1/L[k][k])*(A[k][i]-sumation)
            '''
            if L[i][i]==0:
                return ["There is a cero in L diagonal"]
            U[i][j]=(A[i][j]-np.dot(L[i,1:i-1],U[1:i-1,j]))/L[i][i]

        resultMatrix.append("U") 
        resultMatrix.append(np.array2string(np.around(A,decimals=2)))


    
    resultMatrix.append(str("Stage {} -------------").format(matrixSize[0]))
    resultMatrix.append(np.array2string(np.around(A,decimals=2)))
    z=x=np.linalg.solve(L,b)
    x=x=np.linalg.solve(U,z)
    resultMatrix.append("Result Matrix-------------")   
    resultMatrix.append(np.array2string(np.around(x,decimals=2))) 
    return resultMatrix


def forwardSubs(A,b):
    M=np.append(A,b)
    n=M.shape[0]
    x=np.zeros(n)

    x[0]=M[0][n]/M[0][0]
    for i in range(1,n):
        aux=np.hstack(1,np.matrix.transpose(x[0:i]))
        aux1=np.hstack(M[i][n],-M[i,0:i])
        x[i]=np.dot(aux,aux1)/M[i][i]
    return x

def back_substitution(A, b):
    M=np.append(A,b)
    n=M.shape[0]
    x=np.zeros(n)

    x[n-1]=M[n-1][n]/M[n-1][n-1]
    for i in range(n-1,-1,-1):
        aux=np.hstack(1,x[i+1:n])
        aux1=np.hstack(M[i][n],-M[i][i+1:n])
        x[i]=np.dot(aux,aux1)/M[i][i]
    return x
    



'''
A="[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]"


b="[1],[1],[1],[1]"


crout([A,b])
'''
        
        


