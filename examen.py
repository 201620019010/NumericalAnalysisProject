import numpy as np
import math

A=np.array([
    [300,6,100,1000],
    [6,50,200,-35],
    [100,200,200,14],
    [1000,-35,14,300]
])

D=np.array([
    [0,0,100,1000],
    [0,50,200,14],
    [100,200,200,0],
    [1000,-35,14,300]
])

E=np.array([
    [300,6,0,0],
    [6,0,0,0],
    [0,0,0,14],
    [0,0,14,300]
])

T=-1*(np.linalg.inv(D))
T=np.matmul(T,E)
np.set_printoptions(suppress=True)
print(T)