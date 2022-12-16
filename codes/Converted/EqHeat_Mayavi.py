""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# EqHeat.py: solves heat equation via finite differences, 3-D plot

from numpy import *
import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D
import numpy
from mayavi.mlab import *

Nx = 101
Nt = 9000
Dx = 0.01
Dt = 0.3
KAPPA = 210.0
SPH = 900.0
# conductivity, specf heat, density
RHO = 2700.0  
T = zeros((Nx, 2), float)
Tpl = zeros((Nx, 31), float)

print("Working, wait for figure after count to 10")

for ix in range(1, Nx - 1):
    T[ix, 0] = 100.0
    # initial temperature
T[0, 0] = 0.0
# first and last points at 0
T[0, 1] = 0.0  
T[Nx - 1, 0] = 0.0
T[Nx - 1, 1] = 0.0
cons = KAPPA / (SPH * RHO) * Dt / (Dx * Dx)
# constant
# counter for rows, one every 300 time steps
m = 1  

# time iteration
for t in range(1, Nt):  
# Finite differences
    for ix in range(1, Nx - 1):  
        T[ix, 1] = T[ix, 0] + cons * (T[ix + 1, 0] + T[ix - 1, 0] - 2.0 * T[ix, 0])
# for t = 1 and every 300 time steps
    if t % 300 == 0 or t == 1:  
        for ix in range(1, Nx - 1, 2):
            Tpl[ix, m] = T[ix, 1]
        print(m)
# increase m every 300 time steps
        m = m + 1  
    for ix in range(1, Nx - 1):
# 100 positons at t=m
        T[ix, 0] = T[ix, 1]  
# plot every other x point
x = list(range(1, Nx - 1, 2))  
# every 10 points in y (time)
y = list(range(1, 30))  
# grid for position and time
X, Y = p.meshgrid(x, y)  


# Function returns temperature
def functz(Tpl):  
    z = Tpl[X, Y]
    return z


s = surf(x, y, Tpl)
# Z = functz(Tpl)
# create figure
fig = p.figure()  
# ax = Axes3D(fig)                                             # plots axis
# ax.plot_wireframe(X, Y, Z, color = 'r')                   # red wireframe
# ax.set_xlabel('Position')                                    # label axes
# ax.set_ylabel('time')
# ax.set_zlabel('Temperature')
# shows figure, close Python shell
p.show()  
print("finished")