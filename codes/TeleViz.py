""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# TelegraphViz.py:  Lossless transmission line animation, Visual

from vpython import *
from numpy import *

g = canvas(width=600, height=300, title="Telegrapher`s Eqnt")
vibst = curve(pos=[(x, 0, 0) for x in range(101)], color=color.yellow, radius=0.5)
L = 0.1
C = 2.5
c = 1 / sqrt(L * C)
dt = 0.025
dx = 0.05
# R  = 1 for stabiity
R = (c * dt / dx) ** 2
# Declare array
V = zeros((101, 3), float)
xx = 0

for i in range(0, 100):
    V[i, 0] = 10 * exp(-(xx**2) / 0.1)
    xx = xx + dx
    # i=0-> x=-100;  i =100, x=100
    # Eliminate a curve
    vibst.modify(i, x=2.0 * i - 100.0, y=0)

for i in range(1, 100):
    V[i, 2] = V[i, 0] + R * (V[i + 1, 1] + V[i - 1, 1] - 2 * V[i, 1])
    #  x scale again
    vibst.modify(i, x=2.0 * i - 100.0, y=V[i, 2])

V[:, 0] = V[:, 1]
# Recycle array
V[:, 1] = V[:, 2]

while True:
    # Delay plot, large = slow
    rate(20)
    for i in range(1, 100):
        V[i, 2] = (
            2.0 * V[i, 1] - V[i, 0] + R * (V[i + 1, 1] + V[i - 1, 1] - 2 * V[i, 1])
        )
        # Scale x
        vibst.modify(i, x=2.0 * i - 100.0, y=V[i, 2])
    V[:, 0] = V[:, 1]
    # Recycle array
    V[:, 1] = V[:, 2]
