""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# CircPolarztn.py: Maxwell eqs. for circular polarization using FDTD

from vpython import *
from numpy import *

scene = canvas(
    x=0,
    y=0,
    width=600,
    height=400,
    range=200,
    title="Circular Polarized E (white) & H (yellow) Fields",
)
global phy, pyx
max = 201
# Courant stable if c < 0.1
c = 0.01
Ex = zeros((max + 2, 2), float)
Ey = zeros((max + 2, 2), float)
Hy = zeros((max + 2, 2), float)
Hx = zeros((max + 2, 2), float)
arrowcol = color.white
Earrows = []
Harrows = []
for i in range(0, max, 10):
    Earrows.append(
        arrow(pos=vector(0, i - 100, 0), axis=vector(0, 0, 0), color=arrowcol)
    )
    Harrows.append(
        arrow(pos=vector(0, i - 100, 0), axis=vector(0, 0, 0), color=color.yellow)
    )


def plotfields(Ex, Ey, Hx, Hy):
    for n, arr in enumerate(Earrows):
        arr.axis = vector(35 * Ey[10 * n, 1], 0, 35 * Ex[10 * n, 1])
    for n, arr in enumerate(Harrows):
        arr.axis = vector(35 * Hy[10 * n, 1], 0, 35 * Hx[10 * n, 1])


# Initial E & H
def inifields():
    phx = 0.5 * pi
    phy = 0.0
    z = arange(0, max)
    Ex[:-2, 0] = cos(-2 * pi * z / 200 + phx)
    Ey[:-2, 0] = cos(-2 * pi * z / 200 + phy)
    Hx[:-2, 0] = cos(-2 * pi * z / 200 + phy + pi)
    Hy[:-2, 0] = cos(-2 * pi * z / 200 + phx)


def newfields():
    # Time stepping
    while True:
        rate(1000)
        Ex[1 : max - 1, 1] = Ex[1 : max - 1, 0] + c * (Hy[: max - 2, 0] - Hy[2:max, 0])
        Ey[1 : max - 1, 1] = Ey[1 : max - 1, 0] + c * (Hx[2:max, 0] - Hx[: max - 2, 0])
        Hx[1 : max - 1, 1] = Hx[1 : max - 1, 0] + c * (Ey[2:max, 0] - Ey[: max - 2, 0])
        Hy[1 : max - 1, 1] = Hy[1 : max - 1, 0] + c * (Ex[: max - 2, 0] - Ex[2:max, 0])
        # Periodic BC
        Ex[0, 1] = Ex[0, 0] + c * (Hy[200 - 1, 0] - Hy[1, 0])
        Ex[200, 1] = Ex[200, 0] + c * (Hy[200 - 1, 0] - Hy[1, 0])
        Ey[0, 1] = Ey[0, 0] + c * (Hx[1, 0] - Hx[200 - 1, 0])
        Ey[200, 1] = Ey[200, 0] + c * (Hx[1, 0] - Hx[200 - 1, 0])
        Hx[0, 1] = Hx[0, 0] + c * (Ey[1, 0] - Ey[200 - 1, 0])
        Hx[200, 1] = Hx[200, 0] + c * (Ey[1, 0] - Ey[200 - 1, 0])
        Hy[0, 1] = Hy[0, 0] + c * (Ex[200 - 1, 0] - Ex[1, 0])
        Hy[200, 1] = Hy[200, 0] + c * (Ex[200 - 1, 0] - Ex[1, 0])
        plotfields(Ex, Ey, Hx, Hy)
        Ex[:max, 0] = Ex[:max, 1]
        # Update
        Ey[:max, 0] = Ey[:max, 1]
        Hx[:max, 0] = Hx[:max, 1]
        Hy[:max, 0] = Hy[:max, 1]


# Initial
inifields()
# New
newfields()
