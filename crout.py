import numpy as np 
#import matlab.engine 
#import matlab


def crout(parameters):
    #mlengine=matlab.engine.start_matlab()

    A=eval(parameters[0])
    b=eval(parameters[1])
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
    resultMatrix.append(np.array2string(A))


    for i in range(matrixSize[0]-1):
        #print("Stage ",i+1,"-------------------")
        resultMatrix.append(("Stage ",i+1,"-------------------"))

        dotL=np.zeros(i)
        dotU=np.zeros(i)
        for j in range(i,matrixSize[0]):
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
        
            
            
        resultMatrix.append(np.array2string(L))

        for j in range(i+1,matrixSize[0]):
            '''
            sumation=0
            for p in range(k-1):
                sumation=sumation+(L[k][p]*U[p][i])
            
            U[i][j]=(1/L[k][k])*(A[k][i]-sumation)
            '''

            U[i][j]=(A[i][j]-np.dot(L[i,1:i-1],U[1:i-1,j]))/L[i][i]
        resultMatrix.append(np.array2string(U))
    return resultMatrix

'''
A="[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]"


b="[1],[1],[1],[1]"


crout([A,b])
'''
        
        


