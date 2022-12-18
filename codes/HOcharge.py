""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# HOcharge.py: Quantum particle in HO & E field with Visual

from vpython import *
import numpy as np

# Initialize psi, probability, potential
dx = 0.04
dx2 = dx * dx
k0 = 5.5 * pi
dt = dx2 / 20.0
xmax = 6.0
# Array x positions
xs = arange(-xmax, xmax + dx / 2, dx)
# Magnitude E field
E = 210
g = canvas(
    width=500, height=250, title="Wave packet,harmonic well plus E field", range=10
)
PlotObj = curve(pos=[(x, 0, 0) for x in xs], color=color.yellow, radius=0.1)
g.center = vector(0, 2, 0)

# Initial psi, V
# Re part psi
psr = np.exp(-0.5 * (xs / 0.5) ** 2) * np.cos(k0 * xs)
# Im part psi
psi = np.exp(-0.5 * (xs / 0.5) ** 2) * np.sin(k0 * xs)
# Electric potential
V = 25.0 * xs**2 - E * xs

# Solution as time transpires
while True:
    rate(500)
    psr[1:-1] = (
        psr[1:-1]
        - (dt / dx2) * (psi[2:] + psi[:-2] - 2 * psi[1:-1])
        + dt * V[1:-1] * psi[1:-1]
    )
    psi[1:-1] = (
        psi[1:-1]
        + (dt / dx2) * (psr[2:] + psr[:-2] - 2 * psr[1:-1])
        - dt * V[1:-1] * psr[1:-1]
    )
    y = 4 * (psr**2 + psi**2)
    for i in range(len(y)):
        PlotObj.modify(i, y=y[i])
