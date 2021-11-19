import numpy as np
def functionEvaluator(parameters):
    x = range(eval(parameters[1]),eval(parameters[2]))

    # the function, which is y = x^2 here
    f= eval("lambda x:"+parameters[0])

    points=[]
    for item in x:
        y=f(item)
        points.append(y)
    
    print(points)
    return points