import numpy as np 
import copy

from numpy.core.fromnumeric import diagonal


def gauss(parameters):
    try:
        a=np.array(eval(parameters[0]))
        b=np.array(eval(parameters[1]))
    except Exception as e:
        return ["Wrong Parameters Entered"]

    try:
        arr=np.append(a,b,1)
    except ValueError:
        return ["Matrixes Have different size method fail"]
        
    arrSize=arr.shape
    height=arrSize[0]
    length=arrSize[1]
    responseArr=[]

     
    diagonal=np.diagonal(arr)
    determinant=np.linalg.det(arr)
    if determinant==0:
        return ["Determinant of matrix cant be zero"]
    if 0 in diagonal:
        return ["There is a zero in the diagonal cant run method"]
    

    responseArr.append("Stage:0--------------------------")
    for i in arr:
        responseArr.append(np.array2string(i))
    


    for i in range(0,length-2):
        responseArr.append(("Stage: ",i+1,"--------------------------"))
        for j in range(i+1,height):
            multi=arr[j,i]/diagonal[i]
            currentRow=arr[j, :]
            previousRow=arr[i, :]
            #aplicamos la formula
            row=currentRow-(multi*previousRow)
            #rermplazamos la fila
            arr[j, :]=row
        for x in arr: 
            responseArr.append(np.array2string(np.around(x,decimals=1)))

    depentVariablesMatrix=arr[:,length-1]
    coefficientMatrix=np.delete(arr,length-1,1)

    x=np.linalg.solve(coefficientMatrix,depentVariablesMatrix)
    
    responseArr.append("Answer Matrix--------------")
    responseArr.append(np.array2string(np.around(x,decimals=1)))
    
    return(responseArr)

'''
a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]
b=[1],[1],[1],[1]


response=gauss(a,b)

for item in response:
    print(item)
'''

