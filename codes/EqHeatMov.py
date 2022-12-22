""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# Note: book uses matplotlib instead of vpython

# EqHeatMov.py Animated heat equation soltn via fine differences

from vpython import *
from vpython import *
import numpy as np

g = canvas(width=600, height=300, title="Cooling of Bar, T(t=0) = 100, T(x=0,L)=0")
# Temperature Curve, its parameters and labels
tempe = curve(pos=[(x, 0, 0) for x in range(0, 101)], color=color.red, radius=1.0)
yax = curve(pos=[(0, -20, 0), (0, 40, 0)], color=color.yellow)
maxT = label(text="100", pos=vector(0, 50, 0), box=0)
minT = label(text="0", pos=vector(0, -25, 0), box=0)
bar = curve(pos=[(-100, -20, 0), (100, -20, 0)], color=color.magenta)
thisbar = label(text="Bar", pos=vector(15, -20, 0), xoffset=15, yoffset=-15)
ball1 = sphere(pos=vector(100, -20, 0), color=color.blue, radius=4)
ball2 = sphere(pos=vector(-100, -20, 0), color=color.blue, radius=4)

# Parameters
# Grid points in x
Nx = 101
# x increment
Dx = 0.01414
# t increment
Dt = 1.0
# Thermal conductivity
KAPPA = 210.0
# Specific heat
SPH = 900.0
# Density
RHO = 2700.0
# Temp @ first 2 times
T = np.zeros((Nx, 2), float)

# Initial temperature in bar
for ix in range(1, Nx - 1):
    T[ix, 0] = 100.0
    # Ends of bar at T = 0
    T[0, 0] = 0.0
    T[0, 1] = 0.0
    T[Nx - 1, 0] = 0.0
    T[Nx - 1, 1] = 0.0

# Constant in algor
cons = KAPPA / (SPH * RHO) * Dt / (Dx * Dx)

tempe_x = 2.0 * np.arange(Nx - 1) - 100.0
tempe_y = 0.8 * T[:, 0] - 20.0
for i in range(0, Nx - 1):
    tempe.modify(i, x=tempe_x[i], y=tempe_y[i])


while 1:
    rate(150)
    for ix in range(1, Nx - 1):
        T[ix, 1] = T[ix, 0] + cons * (T[ix + 1, 0] + T[ix - 1, 0] - 2.0 * T[ix, 0])

    tempe_x = 2.0 * np.arange(Nx) - 100.0
    tempe_y = 0.6 * T[:, 1] - 20.0
    for i in range(0, Nx):
        # 0<x<100 -> -100<x<100
        tempe.modify(i, x=tempe_x[i], y=tempe_y[i])

    for ix in range(1, Nx - 1):
        # Row of 100 positions at t = m
        T[ix, 0] = T[ix, 1]
