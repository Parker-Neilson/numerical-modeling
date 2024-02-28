"""
This code models a cannon ball fired at varying degrees above horizontal.
It uses a simple Euler approximation.
"""

#import libraries
from matplotlib import pyplot as plt
import numpy as np


def main():

    #define constants
    g = 9.8
    th = np.linspace(0.03,np.pi/2,10)
    dt = 0.1
    v = 700
    
    #lists appended to store ranges and thetas
    maxes_th = []
    maxes_range = []

    #loop through the th list of angles
    for i in th:
        #define position lists
        x = [0.1]
        y = [0.1]
        #print(th)
        vx = v * np.cos(i)
        vy = v * np.sin(i)
        #loop until it hits the ground
        while y[-1] > 0.0:
            x.append(x[-1]+vx*dt)
            y.append(y[-1]+vy*dt)
            vs = np.linalg.norm([vx,vy])
            ay = -g + drag(y[-1], vy, vs)
            ax = drag(y[-1], vx, vs)
            vy += ay * dt
            vx += ax * dt
            #print(i)
        #plot the motion
        maxes_th.append(i)
        maxes_range.append(x[-1])
        plt.plot(x,y)
    
    #these adopt the highest value of the maxes list
    top_range = 0
    top_th = 0
    
    #there is a much more efficient way to find the maxes than this, 
    #but I already have this, so...
    for i in range(len(maxes_th)):
        if maxes_range[i]>top_range:
            top_range = maxes_range[i]
            top_th = maxes_th[i]

    print(f"the max range is {top_range} it was fired at {top_th*180/np.pi} degrees")
    plt.show()

def drag(h,v,vs): #input height & v output drag acc
    return -4*10e-5*np.exp(-h/(10e4))*vs*np.abs(v)
i
main()

