#!/usr/bin/python
"""question 3"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from decimal import Decimal

#xplot = np.linspace(0, 30, 10000)


plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('hill climbing')
plt.legend(['t', 't**2', 't**3'])


dx = 0

def function(x):
    square = (x)**2
    sint = np.sin(square/2)
    logg2 = np.log2(x+4)
    y = sint/logg2
    return y

#increase the step size

def Hillclimbing():
    #increase the step size
    while dx < round(0.1,1):
        dx += round(0.01,2)
        xstart=x = 0
        #increase the starting position
        while xstart <= 10:
            #reinitialize

            step = 0

            yOP=yPOP= function(x)
            plt.plot(x, yOP, 'r.')

            #loop while yOP is increasing and x is less than 10
            while (yOP>yPOP and x <= 10) or step == 0:

                neighbours = set()
                if round(x-dx, 2)>=0:
                    neighbours.add(round(x-dx,2))
                if round(x+dx, 2)>= 0:
                    neighbours.add(round(x+dx,2))
                step += 1
                print(step)
                xtemp=x
                yPOP = yOP
                #explore all the neighbours
                for xn in list(neighbours):
                    y = function(xn+xtemp)
                    neighbours.remove(xn)
                    if yOP < y:
                        yOP = y
                        x = xn + xtemp
                        plt.plot(xn+xtemp, y, 'r.')
                    #TODO plateau?
                    elif yOP == y:
                        pass
            plt.show()
            xstart+=1
            x=xstart

Hillclimbing()

    
    



