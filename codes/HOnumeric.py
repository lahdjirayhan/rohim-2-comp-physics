""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# HOnumeric.py: 1-D HO wave functions via rk4

import numpy as np, matplotlib.pylab as plt
from rk4Algor import rk4Algor

# x values for plot
rVec = np.zeros((1000), float)
# Wave function values
psiVec = np.zeros((1000), float)
fVec = [0] * (2)
# Declare dimensions
y = [0] * (2)
# n = npr L+1
n = 6


# ODE RHS
def f(x, y):
    fVec[0] = y[1]
    fVec[1] = -(2 * n + 1 - x**2) * y[0]
    return fVec


if n % 2 == 0:
    # Set parity
    y[0] = 1e-8
else:
    y[0] = -1e-8
y[1] = 1.0
i = 0
# RHS at r = 0
f(0.0, y)
dr = 0.01
# Compute WF steps of dr
for r in np.arange(-5, 5, dr):
    rVec[i] = r
    y = rk4Algor(r, dr, 2, y, f)
    psiVec[i] = y[0]
    # Advance i & r
    i = i + 1
plt.figure()
plt.plot(rVec, psiVec)
plt.grid()
plt.title("Harmonic Oscillator Wave Function n = 6")
plt.xlabel("x")
plt.ylabel("$\psi(x)$")
plt.show()
