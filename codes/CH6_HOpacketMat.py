""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# HOpacketMat.py: HO Wave Packet wi Matplotlib Animation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Initialization
a = 1
oneoverpi = 1.0 / (np.sqrt(np.pi))

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-5, 5), ylim=(0, 1.5))
# Plot a grid
ax.grid()
plt.title("Wave Packet in H. O. potential")
plt.xlabel("x")
plt.ylabel(" $|\psi(x,t)|^2$")
(line,) = ax.plot([], [], lw=2)


# base frame
def init():
    line.set_data([], [])
    return (line,)


# Called repeatedly
def animate(t):
    # function to plot every 0.01*t
    y = oneoverpi * np.exp(-((x - a * np.cos(0.01 * t)) ** 2))
    line.set_data(x, y)
    return (line,)


# range for x values
x = np.arange(-5, 5, 0.01)
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=10000, interval=10, blit=True
)
plt.show()
