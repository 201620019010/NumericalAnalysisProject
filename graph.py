import matplotlib.pyplot as plt
import numpy as np
import math
import base64
from PIL import Image
from io import BytesIO


def graphFunction(parameters):
    # 100 linearly spaced numbers
    x = np.linspace(eval(parameters[1]),eval(parameters[2]),100)

    # the function, which is y = x^2 here
    f= eval("lambda x:"+parameters[0])

    points=[]
    for item in x:
        y=f(item)
        points.append(y)


    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(x,points, 'r')

    # show the plot
    plt.savefig('graph.png')

    data=""
    with open('graph.png', "rb") as image_file:
        data = base64.b64encode(image_file.read())
    
    base64String=str(data)
    return base64String[2:len(base64String)-1]
    




f="math.log((math.sin(x)**2)+1)-(1/2)"

graphFunction([f,"-5","5"])

