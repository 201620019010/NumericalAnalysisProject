from gaussianElinimination import gauss 

numericalMethods={
    "gaussianElimination":gauss,

}

def getMethod(key,parameters):
    return numericalMethods[key](parameters)