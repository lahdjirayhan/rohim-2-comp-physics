""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Waves2Danal.py: analytical solution Helmholtz eqn rectangular membrane

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d

t = 0
# speed, tension N/m2, density kg/m2
c = np.sqrt(180.0 / 390.0)  
s5 = np.sqrt(5)
N = 32


def membrane(t, X, Y):
    return np.cos(c * s5 * t) * np.sin(2 * X) * np.sin(Y)


plt.ion()
# Interactive on
fig = plt.figure()  
ax = fig.add_subplot(111, projection="3d")
xs = np.linspace(0, np.pi, 32)
ys = np.linspace(0, np.pi, 32)
X, Y = np.meshgrid(xs, ys)
# x,y grid
Z = membrane(0, X, Y)  
wframe = None
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Vibrating Membrane")

# Total time 10/40
for t in np.linspace(0, 10, 40):  
    oldcol = wframe
# Membrane at t !=0
    Z = membrane(t, X, Y)  
# Plot wireframe
    wframe = ax.plot_wireframe(X, Y, Z)  
# Remove old frame
    if oldcol is not None:  
        ax.collections.remove(oldcol)
# Plot new frame
    plt.draw()  
