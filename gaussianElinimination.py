import numpy as np 
import copy

def gauss(a,b):
    arr=np.append(a,b,1)
    arrSize=arr.shape
    height=arrSize[0]
    length=arrSize[1]
    responseArr=[]
     
    diagonal=np.diagonal(arr)
    while 0 in diagonal:
        zeroIndex=diagonal.tolist().index(0)
        rowToChange=copy.deepcopy(arr[zeroIndex,:])
        rowToChange2=copy.deepcopy(arr[zeroIndex+1,:])

        arr[zeroIndex,:]=rowToChange2
        arr[zeroIndex+1,:]=rowToChange

        diagonal=np.diagonal(arr)

    #print("Stage:0--------------------------")
    #print(arr)

    for i in range(0,length):
        #print("Stage: ",i+1,"--------------------------")
        for j in range(i+1,height):
            multi=arr[j,i]/diagonal[i]
            currentRow=arr[j, :]
            previousRow=arr[i, :]
            #aplicamos la formula
            row=currentRow-(multi*previousRow)
            #rermplazamos la fila
            arr[j, :]=row

        #print(arr)
        responseArr.append(arr)

    depentVariablesMatrix=arr[:,length-1]
    coefficientMatrix=np.delete(arr,length-1,1)

    x=np.linalg.solve(coefficientMatrix,depentVariablesMatrix)
    responseArr.append(x)
    print (x[0])
    return(x)

'''
a=np.array(
   [[-1,  1, -1,  1],
 [ 0 , 0 , 0 , 1],
 [27 , 9 , 3 , 1],
 [64 ,16,  4 , 1]]
)

b=np.array(
    [
    [15.5],
    [3],
    [8],
    [1]
    ]
)


gauss(a,b)

'''