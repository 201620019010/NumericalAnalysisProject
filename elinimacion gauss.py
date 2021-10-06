import numpy as np 

def gauss(a,b):
    arr=np.append(a,b,1)
    arrSize=arr.shape
    height=arrSize[0]
    length=arrSize[1]
     
    diagonal=np.diagonal(arr)

    for i in range(0,length):
        for j in range(i+1,height):
            multi=arr[j,i]/diagonal[i]
            currentRow=arr[j, :]
            previousRow=arr[i, :]
            #aplicamos la formula
            row=currentRow-(multi*previousRow)
            #rermplazamos la fila
            arr[j, :]=row

        #print(arr)
    depentVariablesMatrix=arr[:,length-1]
    coefficientMatrix=np.delete(arr,length-1,1)

    x=np.linalg.solve(coefficientMatrix,depentVariablesMatrix)
    print (x[0])

            

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



gauss(a,b)