import numpy as np 
import copy

def pivoteo_total(a,b):
    arr=np.append(a,b,1)
    arrSize=arr.shape
    height=arrSize[0]
    length=arrSize[1]
     
    diagonal=np.diagonal(arr)
    subMatrix=arr

    for i in range(0,length):
        
        ##################Pivoteo############################################
        if i<length-1:
            if i != 0:
                subMatrix=arr[i:length,i:height]
            else:
                subMatrix=np.delete(arr,length-1,1)
            #print (subMatrix)
            arraymax=np.amax(subMatrix)
            

            maxIndex=np.where(arr==arraymax)
            maxIndex=list(zip(maxIndex[0],maxIndex[1]))
            maxIndex=maxIndex[0]
            ################swaping########################################

            maxIndexRow=copy.deepcopy(arr[maxIndex[0],:])
            rowToExhange=copy.deepcopy(arr[i,:])

            arr[i,:]=maxIndexRow
            arr[maxIndex[0],:]=rowToExhange

        
            maxIndexCol=copy.deepcopy(arr[:,maxIndex[1]])
            colToExchange=copy.deepcopy(arr[:,i])

            arr[:,i]=maxIndexCol
            arr[:,maxIndex[1]]=colToExchange

            
            diagonal=np.diagonal(arr)
            #print(diagonal)
            #print(arr)
        for j in range(i+1,height):
        
            ##################Gauss###################################################
            currentRow=arr[j, :]
            previousRow=arr[i, :]


            multi=arr[j,i]/diagonal[i]
          
        
            #aplicamos la formula
            row=currentRow-(multi*previousRow)
            
            #rermplazamos la fila
            arr[j, :]=row
            #print(arr)

        print(arr)
        
        
    depentVariablesMatrix=arr[:,length-1]
    coefficientMatrix=np.delete(arr,length-1,1)

    x=np.linalg.solve(coefficientMatrix,depentVariablesMatrix)
    #print (x[0])


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