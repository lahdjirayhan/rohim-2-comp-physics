""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# HOpacket.py: HO wave packet in motion via Visual

import numpy as np
from vpython import *

# Constants & Initial Values
oneoverpi = 1 / np.sqrt(np.pi)
# m=1=hbar
a = 1.0
xx = 5
# Initial x & t (classical)
tt = 0
wavef = canvas(x=0, y=0, width=600, height=600, range=8)

x = arange(-5.0, 5.0, 0.001)
plotob = curve(pos=[(x_, 0, 0) for x_ in x], color=color.yellow, radius=0.1)
# Spring
spring = helix(
    pos=vector(-4, -3, 0),
    radius=0.4,
    color=color.white,
    coils=10.4,
    axis=vector(10, 0, 0),
)
mass = box(pos=vector(1, -3, 0), length=1, width=1, height=1, color=color.yellow)

# Time loop
for t in arange(0, 20, 0.1):
    rate(3)
    xx = np.cos(tt)
    y = oneoverpi * np.exp(-((x - a * np.cos(t)) ** 2))
    for i in range(len(x)):
        plotob.modify(i, x=x[i], y=4 * y[i])
    # Classical oscillator
    spring.axis = vector(4 + xx, 0, 0)
    # Position oscillator
    mass.pos = vector(xx, -3, 0)
    tt = tt + 0.1
