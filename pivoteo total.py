import numpy as np 
import copy

def pivoteo_total(A,b):
    arr=np.append(A,b,1)
    arrSize=arr.shape
    height=arrSize[0]
    length=arrSize[1]
    cambi=[]
     
    diagonal=np.diagonal(arr)
    subMatrix=arr
    
    for i in range(length):
        maxIndexes=np.where(abs(arr[i:length,i:length])==max(max(abs(arr[i:length,i:length]))))
        print (maxIndexes)

        
    ''' 
    depentVariablesMatrix=arr[:,length-1]
    coefficientMatrix=np.delete(arr,length-1,1)

    x=np.linalg.solve(coefficientMatrix,depentVariablesMatrix)
    #print (x[0])
    '''


a=np.array(
    [
    [2,-1,0,3],
    [1,0.5,3,8],
    [0,13,-2,11],
    [14,5,-2,3]
    ]
)

b=np.array(
    [
    [1],
    [1],
    [1],
    [1]
    ]
)




pivoteo_total(a,b)