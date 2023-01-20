""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# HOmov: Solve t-dependent Sch Eqt for HO wi animation

import numpy as np
from vpython import *

# Initialize wave function, probability, potential
dx = 0.04
dx2 = dx * dx
k0 = 5.5 * pi
dt = dx2 / 20.0
xmax = 6.0
beta = dt / dx2
# Array x values
xs = arange(-xmax, xmax + dx / 2, dx)

g = canvas(width=500, height=250, title="Wave Packet in HO Well")
PlotObj = curve(pos=[(x, 0, 0) for x in xs], color=color.yellow, radius=0.1)
# Center of scene
g.center = vector(0, 2, 0)
# Initial wave packet
# Array Re I
R = np.exp(-0.5 * (xs / 0.5) ** 2) * np.cos(k0 * xs)
# Array Im I
I = np.exp(-0.5 * (xs / 0.5) ** 2) * np.sin(k0 * xs)
# The potential
V = 15.0 * xs**2

while True:
    rate(1000)
    R[1:-1] = R[1:-1] - beta * (I[2:] + I[:-2] - 2 * I[1:-1]) + dt * V[1:-1] * I[1:-1]
    I[1:-1] = I[1:-1] + beta * (R[2:] + R[:-2] - 2 * R[1:-1]) - dt * V[1:-1] * R[1:-1]
    PlotObj_y = 4 * (R**2 + I**2)
    for i in range(len(xs)):
        PlotObj.modify(i, y=PlotObj_y[i])
