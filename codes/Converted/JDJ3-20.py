# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 04:29:18 2016

@author: mpaez
"""
from scipy import special
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# close to 20*pi, sistance between plates
L = 60  
# position of charge L/2
z0 = 30  
# for positions of z, and r
m = 400  
n = 400
# take constant e/(pi eps0L)=1


# Finds the potential at point (r,z)
def potential(r, z):  
# to sum product
    summ = 0  
# number of terms to find  potential
    for n in range(1, 200):  
# common term in arguments of functions
        ter = n * np.pi / L  
        s1 = np.sin(ter * z0)
        s2 = np.sin(ter * z)
#  k0 Modified Bessel Function
        k0 = special.k0(ter * r)  
        term = s1 * s2 * k0
        summ = summ + term
# value of potential at (r,z)
    return summ  


# value of z interesting region
y = np.arange(29.5, 30.5, 1 / 400.0)  
# values of r that are interesting
x = np.arange(0.0001, 0.4, 0.4 / 400.0)  
X, Y = np.meshgrid(x, y)
#  potential for all values of r and  z
Z = potential(X, Y)  
# to plot the figure
plt.figure()  
# range of levels to plot every 2
levels = np.arange(0o5, 180, 20)  
CS = plt.contour(Z, levels, linewidths=2, extent=(0.001, 0.4, 0, 60))
plt.clabel(CS, inline=1, fmt="%4.1f", fontsize=10)
plt.xlabel("Rho (Distance from z Axis)")
plt.ylabel("Z (Distance Between Plates)")
plt.title("Equipotentia Sufaces, Charge at z = 30, Plates at 0, 60")
plt.plot(0.0, z0, "ro")
plt.show()
