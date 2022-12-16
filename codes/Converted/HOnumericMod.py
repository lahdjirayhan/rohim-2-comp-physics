""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# HOnumeric.py: Quantum HO wave functions via ODE solver

import numpy as np
import matplotlib.pylab as plt
from rk4Algor import rk4Algor

#  Quantum number n = npr + L + 1 = integer > 0
n = 6  
# x values for plot
xx = np.zeros((1000), float)  
# wave function values
yy = np.zeros((1000), float)  
# force function f
fvector = [0] * (2)  
# array for 2 values
y = [0] * (2)  


# Force function for HO
def f(x, y):  
    fvector[0] = y[1]
    fvector[1] = -(2 * n + 1 - x**2) * y[0]
    return fvector


if n % 2 == 0:
    y[0] = 1.0
# Even parity
    y[1] = 0.0  
else:
    y[0] = 0
# Odd parity
    y[1] = 1.0  
# force function at r = 0
f(0, y)  
dr = 0.01
i = 0

# Compute WF from 0 to +5 in steps of dr
for x in np.arange(0, 5, dr):
    xx[i] = x
    y = rk4Algor(x, dr, 2, y, f)
#
    yy[i] = y[0]  
# Advance i as well as r
    i = i + 1  
plt.figure()
plt.plot(xx, yy)
plt.grid()
plt.title("Harmonic Oscillator Wave Function n = xx")
plt.xlabel("x")
plt.ylabel("Wave Function u(x)")
plt.show()
