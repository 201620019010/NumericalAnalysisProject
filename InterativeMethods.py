import math
import numpy as np

def iterativeMethods(A,b,x,iterations,tolerance,chosenMethod):
    D=np.diag(np.diag(A))
    L=np.tril(A,-1)*-1
    U=np.triu(A,1)*-1
    #Jacobi
    if chosenMethod == 1:
        inverseD=np.linalg.inv(D)
        LU=L+U
        Tj=np.matmul(inverseD,LU)
        Cj=np.diag(inverseD*b)

        newX=x
        
        for i in range(iterations):
            print("Tj----------------")
            print(Tj)
            print("Cj----------------")
            print(Cj)
            newX=(np.matmul(Tj,newX))+Cj
            print("newX------------")
            print (newX)
        
    if chosenMethod==2:
        DL=D-L
        inverseDL=np.linalg.inv(DL)
        Tg=np.matmul(inverseDL,U)
        Cg=np.matmul(inverseDL,b)
        newX=x
        for i in range(iterations):
            print("Tg----------------")
            print(Tg)
            print("Cg----------------")
            print(Cg)
            newX=(np.matmul(Tg,newX))+Cg
            print("newX------------")
            print (newX)
            

        


A=np.array(
    [
        [8,3,5],
        [-2,7,3],
        [4,-5,18]
    ]
)

b=np.array(
    [
        21,7,42
    ]   
)

x=np.array([0,0,0])

iterativeMethods(A,b,x,10,10e-7,2)