""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# ForcedOsc.py Driven Oscillator with Mathplotlib

import numpy as np
import matplotlib.pylab as plt
from rk4Algor import rk4Algor

F = 1
m = 1
mu = 0.001
omegaF = 2
# Constants
k = 1  
# Natural frequency
omega0 = np.sqrt(k / m)  
tt = np.zeros((10000), float)
# Init
yPlot = np.zeros((10000), float)  


# RHS force function
def f(t, y):  
# Set up 2D array
    freturn = [0] * (2)  
    freturn[0] = y[1]
    freturn[1] = 0.1 * np.cos(omegaF * t) / m - mu * y[1] / m - omega0**2 * y[0]
    return freturn


# Set up 2D array
y = [0] * (2)  
# initial conditions:x
y[0] = 0.1  
# init cond speed
y[1] = 0.3  
# call function for t=0 with init conds.
f(0, y)  
dt = 0.01
i = 0
for t in np.arange(0, 100, dt):
    tt[i] = t
# call runge kutta
    y = rk4Algor(t, dt, 2, y, f)  
# can change to yy[i]=y[1] to plot velocity
    yPlot[i] = y[0]  
    i = i + 1
plt.figure()
plt.plot(tt, yPlot)
plt.title("$\omega_f$=2,k=1,m=1,$\omega_0$=1,$\lambda = 0.001$")
plt.xlabel("t")
plt.ylabel("x")
plt.show()
