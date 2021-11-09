import numpy as np
from gaussianElinimination import gauss
from gaussian import eliminacion

y = np.array(
    [
        [15.5],
        [3],
        [8],
        [1]
    ]
    )
x = np.array([-1,0,3,4])

print("Vandermonde Matrix-------------------")
print(np.vander(x))
print("Polinome Coefficients----------------")
polinome=gauss(np.vander(x),y)
print(polinome)

print("\n")

