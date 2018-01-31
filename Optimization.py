#!/usr/bin/python
"""question 3"""

#import matplotlib.pyplot as plt
#import matplotlib as mpl
import numpy as np
import math
from decimal import Decimal
import random

#xplot = np.linspace(0, 30, 10000)
#plt.legend(['t', 't**2', 't**3'])


#TODO convert to decimal?
def function(x):
    square = (x)**2
    sint = np.sin(square/2)
    log2 = np.log2(x+4)
    y = sint/log2
    return y

#increase the step size
#choose tempStart and 0 < tempC < 1
def annealing(tempC, tempStart):
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
            yLocal=yPrevLocal= function(x)
            temp = tempStart
            boltP = 1
            #plt.plot(x, yLocal, 'r.')
            yGlobal=xGlobal = 0

            #Change until boltzman probability goes to 0 and x less than 10
            while (boltP>0  and x <= 10) or step == 0:
                temp = temp * tempC
                
                neighbours = []
                if 0 <= round(x-dx, 2) <= 10:
                    neighbours.append(round(x-dx,2))
                if 0 <= round(x+dx, 2) <= 10:
                    neighbours.append(round(x+dx,2))
                #search neighbour in random order
                randN = random.sample(range(len(neighbours)), len(neighbours))

                #explore all the neighbours
                for neighbour in randN:
                    xn = neighbours[neighbour]
                    y = function(xn)


                    # replace if better local Y
                    if yLocal < y:
                        yLocal = y
                        x = xn
                        if yGlobal < yLocal:
                            yGlobal = yLocal
                            xGlobal = x

                        #plt.plot(xn, y, 'r.')
                        break

                    #with some chance still choose y even if worse
                    elif yLocal > y:
                        boltP = math.exp((-(yLocal-y))/temp)
                        # NOTE To find the best temp to start 
                        # find the biggest difference between ylocal and y
                        # rearrange boltp = 0.95 and find temp
                        
                        select = np.random.choice([True,False], 1, p=[boltP, 1-boltP])
                        if select:
                            yLocal = y
                            x = xn
                            #plt.plot(xn, y, 'b.')
                            break
                        
                    #NOTE plateau
                    else: 
                        pass
                # add one step when climbing after selecting the best neighbour
                step += 1

            """NOTE debugging plot
            plt.xlabel('x-axis step size:'+str(dx))
            plt.ylabel('y-axis')
            plt.title('hill climbing')
            plt.show()
            """
            print('Final X:', x, '| Final Y:', yGlobal, '| Total Steps:',step)
            print('X Start:', xstart, '| X Step Size:', dx)
            xstart+=1
            x=xstart


def annealingSet(tempC, tempStart):
    climbSet = {0.02, 0.04, 0.1}
    xstart = x = 0
    #increase the starting position
    while xstart <= 10:
        #reinitialize
        step = 0
        yLocal = yPrevLocal = function(x)
        temp = tempStart
        boltP = 1
        #plt.plot(x, yLocal, 'r.')
        yGlobal = xGlobal = 0
        #Change until boltzman probability goes to 0 and x less than 10
        while (boltP > 0 and x <= 10) or step == 0:
            temp = temp * tempC
            neighbours = [] 
            for dx in climbSet:
                if 0 <= round(x-dx, 2) <= 10:
                    neighbours.append(round(x-dx, 2))
                if 0 <= round(x+dx, 2) <= 10:
                    neighbours.append(round(x+dx, 2))
            #search neighbour in random order
            randN = random.sample(range(len(neighbours)), len(neighbours))
            
            #explore all the neighbours
            for neighbour in randN:
                xn = neighbours[neighbour]
                y = function(xn)
                # replace if better local Y
                if yLocal < y:
                    yLocal = y
                    x = xn
                    if yGlobal < yLocal:
                        yGlobal = yLocal
                        xGlobal = x
                
                    #plt.plot(xn, y, 'r.')
                    break
                #with some chance still choose y even if worse
                elif yLocal > y:
                    boltP = math.exp((-(yLocal-y))/temp)
                    # NOTE To find the best temp to start
                    # find the biggest difference between ylocal and y
                    # rearrange boltp = 0.95 and find temp
                    select = np.random.choice(
                        [True, False], 1, p=[boltP, 1-boltP])
                    if select:
                        yLocal = y
                        x = xn
                        #plt.plot(xn, y, 'b.')
                        break
                #NOTE plateau
                else:
                    pass
            # add one step when climbing after selecting the best neighbour
            step += 1
        """NOTE debugging plot
        plt.xlabel('x-axis step size:'+str(dx))
        plt.ylabel('y-axis')
        plt.title('hill climbing')
        plt.show()
        """
        
        print('Final X:', x, '| Final Y:', yGlobal)
        print('X Start:', xstart, '| Total Steps:', step)
        xstart += 1
        x = xstart

    print('Temp start:', tempStrart, '| Temp multiplier:', tempC)


def HillclimbingSet():
    
    climbSet = {0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1}
    xstart = x = 0
    #increase the starting position
    while xstart <= 10:
        #reinitialize
        step = 0
        yOP = yPOP = function(x)
        #plt.plot(x, yOP, 'r.')
        #loop while yOP is increasing and x is less than 10
        while (yOP > yPOP and x <= 10) or step == 0:
            neighbours = []
            for dx in climbSet:
                if 0 <= round(x-dx, 2) <= 10:
                    neighbours.append(round(x-dx,2))
                if 0 <= round(x+dx, 2) <= 10:
                    neighbours.append(round(x+dx,2))
                #search neighbour in random order
            randN = random.sample(range(len(neighbours)), len(neighbours))
            yPOP = yOP
            #Previous x holder
            xP = x
            #explore all the neighbours
            for neighbour in randN:
                xn = neighbours[neighbour]
                y = function(xn)
                if yOP < y:
                    yOP = y
                    x = xn
                    #plt.plot(xn, y, 'r.')
                #NOTE plateau
                elif yOP == y:
                    pass
            #NOTE print out the best step size to use, one with most frequency
            # print('best step size:', round(x-xP,3),' x:',x)
            # add one step when climbing after selecting the best neighbour
            step += 1
        """NOTE debugging plot
        plt.xlabel('x-axis step size:'+str(dx))
        plt.ylabel('y-axis')
        plt.title('hill climbing')
        plt.show()
        """
        print('Final X:', x, '| Final Y:', yOP)
        print('X Start:', xstart, '| Total Steps:', step)
        xstart += 1
        x = xstart

def Hillclimbing():
    dx = 0
    #increase the step size
    while dx < 0.1:
        dx += 0.01
        dx = round(dx, 2)
        xstart = x = 0
        #increase the starting position
        while xstart <= 10:
            #reinitialize
            step = 0
            yOP = yPOP = function(x)
            #plt.plot(x, yOP, 'r.')

            #loop while yOP is increasing and x is less than 10
            while (yOP > yPOP and x <= 10) or step == 0:

                neighbours = set()
                if 0 <= round(x-dx, 2) <= 10:
                    neighbours.add(round(x-dx, 2))
                if 0 <= round(x+dx, 2) <= 10:
                    neighbours.add(round(x+dx, 2))

                yPOP = yOP
                #explore all the neighbours
                for xn in list(neighbours):
                    y = function(xn)
                    neighbours.remove(xn)
                    if yOP < y:
                        yOP = y
                        x = xn
                        #plt.plot(xn, y, 'r.')
                    #NOTE plateau
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
            print('Final X:', x, '| Final Y:', yOP, '| Total Steps:', step)
            print('X Start:', xstart, '| X Step Size:', dx)
            xstart += 1
            x = xstart


#annealing(0.999, 10)
Hillclimbing()
print("Hill Climbing Set")
HillclimbingSet()
print("Annealing Set")
annealingSet(0.999, 10)
print("Annealing Set")
annealingSet(0.99, 10)
print("Annealing Set")
annealingSet(0.9, 10)
print("Annealing Set")
annealingSet(0.999, 1)
print("Annealing Set")
annealingSet(0.99, 1)
print("Annealing Set")
annealingSet(0.9, 1)



    
    



