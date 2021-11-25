import numpy as np 
import copy
np.set_printoptions(suppress=True),

def parcialPivoting(parameters):
    try:
        a=np.array(eval(parameters[0]))
        b=np.array(eval(parameters[1]))
        arr=np.append(a,b,1)
    except ValueError:
        return ["Wrong Parameters Entered"]

    try:
        np.append(a,b,1)
    except ValueError:
        return ["Matrixes Have different size method fail"]

    arrSize=arr.shape
    height=arrSize[0]
    length=arrSize[1]

    responseArr=[]
     
    diagonal=np.diagonal(arr)

    responseArr.append("Stage:0--------------------------")
    for i in arr:
        responseArr.append(np.array2string(np.around(i,decimals=2)))

    for i in range(0,length-2):
        ##################Pivoteo############################################
        diagonal=np.diagonal(arr)

        if 0 in diagonal:
            return ["There is a cero in the submatrix diagonal method failed"]

            
        responseArr.append(("Stage: ",i+1,"--------------------------"))
        if i<length-1:
            column=list(map(abs,arr[:,i]))
            
           

            if i != 0:
                column=column[i:]


            columnMax=max(column)


            maxIndex=column.index(columnMax)+i
            print(columnMax)
            ##copiamos lista por valor no por referencia
            maxIndexRow=copy.deepcopy(arr[maxIndex,:])
            rowToExhange=copy.deepcopy(arr[i,:])
        
            arr[i,:]=maxIndexRow
            arr[maxIndex,:]=rowToExhange
        
        for j in range(i+1,height):
            ##################Gauss###################################################
            currentRow=arr[j, :]
            previousRow=arr[i, :]


            multi=arr[j,i]/diagonal[i]
            
            #aplicamos la formula
            row=currentRow-(multi*previousRow)
            #rermplazamos la fila
            arr[j, :]=row
        for x in arr: 
            responseArr.append(np.array2string(np.around(x,decimals=2)))
        #print(arr)
    depentVariablesMatrix=arr[:,length-1]
    coefficientMatrix=np.delete(arr,length-1,1)

    x=np.linalg.solve(coefficientMatrix,depentVariablesMatrix)

    responseArr.append("Answer Matrix--------------")
    responseArr.append(np.array2string(np.around(x,decimals=2)))
    return(responseArr)

'''
a=[2,-1,0,3],[1,0.5,3,8],[0,13,-2,11],[14,5,-2,3]
b=[1],[1],[1],[1]


response=parcialPivoting(a,b)

for item in response:
    print(item)
'''

