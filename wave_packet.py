import numpy as np
from matplotlib import pyplot as plt

#creates an object that represents a wave on a string
class wave:
    def __init__(self, dt, dx, vi):
        self.dx = dx #small step in x
        self.vi = vi #initil vel
        self.dt = dt #time step
        return None

    def wav_func(self, y0, y1,i):
        c = self.const()
        r = 1 #constant
        y = 2*(1-(r)**2)*y1[i]-y0[i]+r**2*(y1[i+1]+y1[i-1]) #finds y new at a time step
        return y

    def const(self):
        return 1

vi = 1 #v initial
vi2 = -1 #v initial of the second wave
dt = 0.01 #time step
dx = 0.01 #space step
X = np.arange(-2,2,dx) #array represents points on a sting

Y_old = np.exp(-4*(X-0.25)**2) #reps strings points at a previous time step
Y_old2 =  -np.exp(-4*(X-0.75)**2)

Y_current = np.exp(-4*(X-0.25)**2) + dx #reps the strings pos at the current time
Y_current2 = -np.exp(-4*(X-0.75)**2) - dx

t = 0 #counts time
Y1 = wave(dt,dx,vi) #makes a wave object
Y2 = wave(dt,dx,vi2)
counter = 0 #counts the loops of the while loop
while t < 10:
    Y_new = np.zeros_like(X) #makes an array to be filled with new y values
    Y_new2 = np.zeros_like(X)
    for i in range(len(X)):
        if i >= len(X)-1:
            break
        Y_new[i] = Y1.wav_func(Y_old,Y_current,i) #update the object
        Y_new2[i] = Y1.wav_func(Y_old2,Y_current2,i)
    Y_old = np.copy(Y_current) #new points become current
    Y_old2 = np.copy(Y_current2)
    Y_current = Y_new #current points become old
    Y_current2 = Y_new2
    #plot every ten time steps
    if counter%10==0:
        plt.plot(X,Y_current+Y_current2,'r-')
        plt.ylim(-4,4)
        plt.draw()
        plt.pause(0.001)
        plt.clf()
    t += dt
    counter+=1
