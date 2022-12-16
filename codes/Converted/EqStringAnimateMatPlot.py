""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# EqStringAnimateMatPlot.py:  Animated soltn for string waves wi MatPlot

from numpy import *
import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animation

rho = 0.01
ten = 40.0
# string density
c = sqrt(ten / rho)  
c1 = c
# CFL criterium = 1
ratio = c * c / (c1 * c1)  
# 101 x's & 3 t's
xi = np.zeros((101, 3), float)  
k = list(range(0, 101))


# Initial conditions
def Initialize():  
    for i in range(0, 81):
        xi[i, 0] = 0.00125 * i
    for i in range(81, 101):
        xi[i, 0] = 0.1 - 0.005 * (i - 80)


def animate(num):
    for i in range(1, 100):
        xi[i, 2] = ( 2.0 * xi[i, 1] - xi[i, 0] + ratio * (xi[i + 1, 1] + xi[i - 1, 1] - 2 * xi[i, 1]) )
# Data to plot ,x,y
    line.set_data(k, xi[k, 2])  
    for m in range(0, 101):
# Recycle array
        xi[m, 0] = xi[m, 1]  
        xi[m, 1] = xi[m, 2]
    return line


# Plot initial string
Initialize()  
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=vector(0, 101,0), ylim=vector(-0.15, 0.15,0))
# Plot  grid
ax.grid()  
plt.title("Vibrating String")
(line,) = ax.plot(k, xi[k, 0], lw=2)
for i in range(1, 100):
    xi[i, 1] = xi[i, 0] + 0.5 * ratio * (xi[i + 1, 0] + xi[i - 1, 0] - 2 * xi[i, 0])
# Dummy argument: 1
ani = animation.FuncAnimation(fig, animate, 1)  
plt.show()
print("finished")
