#!/usr/bin/python
"""question 3"""

#import matplotlib.pyplot as plt
#import matplotlib as mpl
import numpy as np
from decimal import Decimal

#xplot = np.linspace(0, 30, 10000)
#plt.legend(['t', 't**2', 't**3'])




def function(x):
    square = (x)**2
    sint = np.sin(square/2)
    log2 = np.log2(x+4)
    y = sint/log2
    return y

#increase the step size

def Hillclimbing():
    dx = 0
    #increase the step size
    while dx < 0.1:
        dx += 0.01
        dx = round(dx, 2)
        xstart=x = 0
        #increase the starting position
        while xstart <= 10:
            #reinitialize
            step = 0
            yOP=yPOP= function(x)
            #plt.plot(x, yOP, 'r.')

            #loop while yOP is increasing and x is less than 10
            while (yOP > yPOP and x <= 10) or step == 0:
                neighbours = set()
                if 0 <= round(x-dx, 2) <= 10:
                    neighbours.add(round(x-dx,2))
                if 0 <= round(x+dx, 2) <= 10:
                    neighbours.add(round(x+dx,2))
                yPOP = yOP
                #explore all the neighbours
                for xn in list(neighbours):
                    y = function(xn)
                    neighbours.remove(xn)
                    if yOP < y:
                        yOP = y
                        x = xn
                        #plt.plot(xn, y, 'r.')
                    #TODO plateau?
                    elif yOP == y:
                        pass
                # add one step when climbing after selecting the best neighbour
                step += 1

            """NOTE debugging plot
            plt.xlabel('x-axis step size:'+str(dx))
            plt.ylabel('y-axis')
            plt.title('hill climbing')
            plt.show()
            """
            print('Final X:', x, 'Final Y:', yOP, 'Total Steps:',step)
            print('X Start:', xstart, 'X Step Size:', dx)
            xstart+=1
            x=xstart

Hillclimbing()

    
    



