""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# Note: book uses matplotlib instead of vpython

# GlauberState.py: Glauber's Coherent Quantum State

from numpy import *
from vpython import *
import math

wavef = canvas(x=0, y=0, width=600, height=600, range=50)
plotob = curve(pos=[(x, 0, 0) for x in range(0, 80)], color=color.yellow, radius=0.2)
sqpi = math.sqrt(math.pi)
E = 3.0
# E, Coherent Eigenvalue
alpha = sqrt(E - 0.5)
factr = math.exp(-0.5 * alpha * alpha)


# Hermite polynomial
def Hermite(x, n):
    if n == 0:
        p = 1.0
    elif n == 1:
        p = 2 * x
    else:
        p0 = 1
        p1 = 2 * x
        for i in range(1, n):
            p2 = 2 * x * p1 - 2 * i * p0
            p0 = p1
            p1 = p2
            p = p2
    return p


# Coherent state
def glauber(x, t, nmax):
    Reterm = 0.0
    Imterm = 0.0
    factr = math.exp(-0.5 * alpha * alpha)
    for n in range(0, nmax):
        fact = math.sqrt(1.0 / (math.factorial(n) * sqpi * (2**n)))
        psin = fact * Hermite(x, n) * math.exp(-0.5 * x * x)
        den = sqrt(math.factorial(n))
        num = factr * (alpha**n) * psin
        Reterm += num * (math.cos((n + 0.5) * t)) / den
        Imterm += num * (math.sin((n + 0.5) * t)) / den
    phi = math.sqrt(Reterm * Reterm + Imterm * Imterm)
    return phi


def motion(nmax):
    for t in arange(0, 18.0, 0.03):
        xx = -8.0
        for i in range(0, 80):
            # Find coherent state
            y = glauber(xx, t, nmax)
            # Plot state
            plotob.modify(i, x=4 * xx, y=15 * y)
            xx += 0.2


# Parameter: max degree Hn
motion(20)
