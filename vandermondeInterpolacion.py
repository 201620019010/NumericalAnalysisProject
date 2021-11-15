import numpy as np
from gaussianElinimination import gauss
#from gaussian import eliminacion
'''
y = np.array(
    [
        [-5.04],
        [-1.47],
        [-1.69],
        [10.89]
    ]
    )
x = np.array([0.5,1,3,5])
'''
def vandermonde(parameters):
    x=np.array(eval(parameters[0]))
    resultMatrix=[]

    resultMatrix.append("Vandermonde Matrix-------------------")
    resultMatrix.append(np.array2string(np.vander(x)))

    resultMatrix.append("Polinome Coefficients----------------")


    vandermonde=np.array2string(np.vander(x),separator=",")

    polinome=gauss([vandermonde,parameters[1]])
    length=len(polinome)
    resultMatrix.append(polinome[length-4])
    resultMatrix.append(polinome[length-3])
    resultMatrix.append(polinome[length-2])
    resultMatrix.append(polinome[length-1])

    return resultMatrix


