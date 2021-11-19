import numpy as np 

def doolittle(parameters):
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
    L=np.identity(matrixSize[0])
    U=np.identity(matrixSize[0])

    resultMatrix.append("Stage 0 --------------------------")
    for x in A:
        resultMatrix.append(np.array2string(x))

    for i in range(matrixSize[0]-1):
        resultMatrix.append(("Stage ",i+1,"-------------------"))
        for j in range(i,matrixSize[0]):
            U[i,j]=A[i,j]-np.dot(L[i,1:i-1],U[1:i-1,j])

        resultMatrix.append("U")  
        for x in U:
            resultMatrix.append(np.array2string(x)) 

        for j in range(i+1,matrixSize[0]):
            L[j,i]=(A[j][i]-np.dot(L[j,1:i-1],U[1:i-1,i]))/U[i][i]

        resultMatrix.append("L")  
        for x in L:
            resultMatrix.append(np.array2string(x)) 
    
    return resultMatrix



    
A="[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]"


b="[1],[1],[1],[1]"


print (doolittle([A,b]))
