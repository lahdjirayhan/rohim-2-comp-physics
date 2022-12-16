""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# QuantumEigen.py:             Finds E and psi via rk4 + bisection

# mass/((hbar*c)**2)= 940MeV/(197.33MeV-fm)**2 =0.4829
# well width=20.0 fm, depth 10 MeV, Wave function not normalized.

from visual import *

psigr = canvas(x=0, y=0, width=600, height=300, title="R & L Wavefunc")
Lwf = curve(x=list(range(502)), color=color.red)
Rwf = curve(x=list(range(997)), color=color.yellow)
# Precision
eps = 1e-3  
n_steps = 501
# E guess
E = -17.0  
h = 0.04
count_max = 100
# E limits
Emax = 1.1 * E  
Emin = E / 1.1


def f(x, y, F, E):
    F[0] = y[1]
    F[1] = -(0.4829) * (E - V(x)) * y[0]


def V(x):
    if abs(x) < 10.0:
# Well depth
        return -16.0  
    else:
        return 0.0


def rk4(t, y, h, Neqs, E):
    F = zeros((Neqs), float)
    ydumb = zeros((Neqs), float)
    k1 = zeros((Neqs), float)
    k2 = zeros((Neqs), float)
    k3 = zeros((Neqs), float)
    k4 = zeros((Neqs), float)
    f(t, y, F, E)
    for i in range(0, Neqs):
        k1[i] = h * F[i]
        ydumb[i] = y[i] + k1[i] / 2.0
    f(t + h / 2.0, ydumb, F, E)
    for i in range(0, Neqs):
        k2[i] = h * F[i]
        ydumb[i] = y[i] + k2[i] / 2.0
    f(t + h / 2.0, ydumb, F, E)
    for i in range(0, Neqs):
        k3[i] = h * F[i]
        ydumb[i] = y[i] + k3[i]
    f(t + h, ydumb, F, E)
    for i in range(0, Neqs):
        k4[i] = h * F[i]
        y[i] = y[i] + (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6.0


def diff(E, h):
    y = zeros((2), float)
# Matching radius
    i_match = n_steps // 3  
    nL = i_match + 1
    y[0] = 1.0e-15
    # Initial left wf
    y[1] = y[0] * sqrt(-E * 0.4829)
    for ix in range(0, nL + 1):
        x = h * (ix - n_steps / 2)
        rk4(x, y, h, 2, E)
# Log  derivative
    left = y[1] / y[0]  
    y[0] = 1.0e-15
    # For even;  reverse for odd
# Initialize R wf
    y[1] = -y[0] * sqrt(-E * 0.4829)  
    for ix in range(n_steps, nL + 1, -1):
        x = h * (ix + 1 - n_steps / 2)
        rk4(x, y, -h, 2, E)
# Log derivative
    right = y[1] / y[0]  
    return (left - right) / (left + right)


# Repeat integrations for plot
def plot(E, h):  
    x = 0.0
# # integration steps
    n_steps = 1501  
    y = zeros((2), float)
    yL = zeros((2, 505), float)
# Matching point
    i_match = 500  
    nL = i_match + 1
# Initial left wf
    y[0] = 1.0e-40  
    y[1] = -sqrt(-E * 0.4829) * y[0]
    for ix in range(0, nL + 1):
        yL[0][ix] = y[0]
        yL[1][ix] = y[1]
        x = h * (ix - n_steps / 2)
        rk4(x, y, h, 2, E)
# For even;  reverse for odd
    y[0] = -1.0e-15  
    y[1] = -sqrt(-E * 0.4829) * y[0]
    j = 0
# right WF
    for ix in range(n_steps - 1, nL + 2, -1):  
# Integrate in
        x = h * (ix + 1 - n_steps / 2)  
        rk4(x, y, -h, 2, E)
        Rwf.x[j] = 2.0 * (ix + 1 - n_steps / 2) - 500.0
        Rwf.y[j] = y[0] * 35e-9 + 200
        j += 1
    x = x - h
    normL = y[0] / yL[0][nL]
    j = 0
    # Renormalize L wf & derivative
    for ix in range(0, nL + 1):
        x = h * (ix - n_steps / 2 + 1)
        y[0] = yL[0][ix] * normL
        y[1] = yL[1][ix] * normL
        Lwf.x[j] = 2.0 * (ix - n_steps / 2 + 1) - 500.0
# Factor for scale
        Lwf.y[j] = y[0] * 35e-9 + 200  
        j += 1


for count in range(0, count_max + 1):
# Slow rate to show changes
    rate(1)  
    # Iteration loop
# Divide E range
    E = (Emax + Emin) / 2.0  
    Diff = diff(E, h)
    if diff(Emax, h) * Diff > 0:
# Bisection algor
        Emax = E  
    else:
        Emin = E
    if abs(Diff) < eps:
        break
# First iterates too irregular
    if count > 3:  
        rate(4)
        plot(E, h)
    elabel = label(pos=vector(700, 400,0), text="E=", box=0)
    elabel.text = "E=%13.10f" % E
    ilabel = label(pos=vector(700, 600,0), text="istep=", box=0)
    ilabel.text = "istep=%4s" % count
# Last iteration
elabel = label(pos=vector(700, 400,0), text="E=", box=0)  
elabel.text = "E=%13.10f" % E
ilabel = label(pos=vector(700, 600,0), text="istep=", box=0)
ilabel.text = "istep=%4s" % count

print(("Final eigenvalue E = ", E))
print(("iterations, max = ", count))
