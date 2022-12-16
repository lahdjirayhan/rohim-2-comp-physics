""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Bessel.py
from vpython import *
from vpython import *

Xmax = 40.0
Xmin = 0.25
step = 0.1  # Global class variables
order = 10
start = 50  # Plot j_order
graph1 = gdisplay(
    width=500,
    height=500,
    title="Sperical Bessel, \
       L = 1 (red), 10",
    xtitle="x",
    ytitle="j(x)",
    xmin=Xmin,
    xmax=Xmax,
    ymin=-0.2,
    ymax=0.5,
)
funct1 = gcurve(color=color.red)
funct2 = gcurve(color=color.green)


def down(x, n, m):  # Method down, recurs downward
    j = zeros((start + 2), float)
    j[m + 1] = j[m] = 1.0  # Start with anything
    for k in range(m, 0, -1):
        j[k - 1] = ((2.0 * k + 1.0) / x) * j[k] - j[k + 1]
    scale = (sin(x) / x) / j[0]  # Scale solution to known j[0]
    return j[n] * scale


for x in arange(Xmin, Xmax, step):
    funct1.plot(pos=(x, down(x, order, start)))

for x in arange(Xmin, Xmax, step):
    funct2.plot(pos=(x, down(x, 1, start)))