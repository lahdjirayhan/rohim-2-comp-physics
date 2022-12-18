""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# Note: book uses matplotlib instead of vpython

# QuantumEigenCall.py: Finds E & psi via rk4 + bisection

# m/(hbar*c)**2 = 940MeV/(197.33MeV-fm)**2 = 0.4829
from vpython import *
import numpy as np
from rk4Algor import rk4Algor

psigr = canvas(x=0, y=0, width=600, height=300, title="R & L Psi")
Lwf = curve(pos=[(x, 0, 0) for x in range(502)], color=color.red)
Rwf = curve(pos=[(x, 0, 0) for x in range(997)], color=color.yellow)
eps = 1e-1
Nsteps = 501
h = 0.04
# Search Params
Nmax = 100
E = -17.0
Emax = 1.1 * E
# Init E & limits
Emin = E / 1.1


# RHS for ODE
def f(x, y):
    global E
    F = np.zeros((2), float)
    F[0] = y[1]
    F[1] = -(0.4829) * (E - V(x)) * y[0]
    return F


# Potential
def V(x):
    if abs(x) < 10.0:
        return -16.0
    else:
        return 0.0


# Change in log deriv
def diff(h):
    global E
    y = np.zeros((2), float)
    # Matching radius
    i_match = Nsteps // 3
    nL = i_match + 1
    y[0] = 1.0e-15
    # Initial left wf
    y[1] = y[0] * sqrt(-E * 0.4829)
    for ix in range(0, nL + 1):
        x = h * (ix - Nsteps / 2)
        y = rk4Algor(x, h, 2, y, f)
    # Log  derivative
    left = y[1] / y[0]
    y[0] = 1.0e-15
    #  Slope for even; reverse if odd
    # Initialize R wf
    y[1] = -y[0] * sqrt(-E * 0.4829)
    for ix in range(Nsteps, nL + 1, -1):
        x = h * (ix + 1 - Nsteps / 2)
        y = rk4Algor(x, -h, 2, y, f)
    # Log derivative
    right = y[1] / y[0]
    return (left - right) / (left + right)


# Repeat integrations for plot
def plot(h):
    global E
    x = 0.0
    # Integration steps
    Nsteps = 1501
    y = np.zeros((2), float)
    yL = np.zeros((2, 505), float)
    # Matching radius
    i_match = 500
    nL = i_match + 1
    # Initial left wf
    y[0] = 1.0e-40
    y[1] = -sqrt(-E * 0.4829) * y[0]
    for ix in range(0, nL + 1):
        yL[0][ix] = y[0]
        yL[1][ix] = y[1]
        x = h * (ix - Nsteps / 2)
        y = rk4Algor(x, h, 2, y, f)
    # - slope: even;  reverse if odd
    y[0] = -1.0e-15
    y[1] = -sqrt(-E * 0.4829) * y[0]
    j = 0
    # Right WF
    for ix in range(Nsteps - 1, nL + 2, -1):
        # Integrate in
        x = h * (ix + 1 - Nsteps / 2)
        y = rk4Algor(x, -h, 2, y, f)
        Rwf_x_j = 2.0 * (ix + 1 - Nsteps / 2) - 500.0
        Rwf_y_j = y[0] * 35e-9 + 200
        Rwf.modify(j, x=Rwf_x_j, y=Rwf_y_j)
        j += 1
    x = x - h
    normL = y[0] / yL[0][nL]
    j = 0
    # Normalize L wf & derivative
    for ix in range(0, nL + 1):
        x = h * (ix - Nsteps / 2 + 1)
        y[0] = yL[0][ix] * normL
        y[1] = yL[1][ix] * normL
        Lwf_x_j = 2.0 * (ix - Nsteps / 2 + 1) - 500.0
        # Factor for scale
        Lwf_y_j = y[0] * 35e-9 + 200
        Lwf.modify(j, x=Lwf_x_j, y=Lwf_y_j)
        j += 1


# Main program
for count in range(0, Nmax + 1):
    # Slow rate shows changes
    rate(1)
    # Bisec E range
    E = (Emax + Emin) / 2.0
    Diff = diff(h)
    Etemp = E
    E = Emax
    diffMax = diff(h)
    E = Etemp
    if diffMax * Diff > 0:
        # Bisection algor
        Emax = E
    else:
        Emin = E
    print("Iteration, E =", count, E)
    if abs(Diff) < eps:
        break
    if count > 3:
        rate(4)
        plot(h)
    elabel = label(pos=vector(700, 400, 0), text="E=", box=0)
    elabel.text = "E=%13.10f" % E
    ilabel = label(pos=vector(700, 600, 0), text="istep=", box=0)
    ilabel.text = "istep=%4s" % count
# Last
elabel = label(pos=vector(700, 400, 0), text="E=", box=0)
elabel.text = "E=%13.10f" % E
ilabel = label(pos=vector(700, 600, 0), text="istep=", box=0)
ilabel.text = "istep=%4s" % count
print("Final eigenvalue E =", E)
print("Iterations = ", count, ", max = ", Nmax)
