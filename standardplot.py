#!/usr/bin/python
"""question 3"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#xplot = np.linspace(0, 30, 10000)

y = 0
x = 0
dx = 0
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('hill climbing')
# plt.legend(['t', 't**2', 't**3'])

while dx < 0.1:
    #BUG TODO rounding issue need fix
    dx += 0.01
    while x <= 10:
        
        square = (x)**2
        sint = np.sin(square/2)
        log2 = np.log2(x+4)
        y = sint/log2

        plt.plot(x, y, 'rs')
        x = x + dx
    plt.show()
    x=0
    



