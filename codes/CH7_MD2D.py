""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# MD2.py:           Molecular dynamics in 2D

from vpython import *
from vpython import *
import random
import numpy as np

scene = canvas(x=0, y=0, width=350, height=350, title="Molecular Dynamics", range=10)
sceneK = graph(
    x=0,
    y=350,
    width=600,
    height=150,
    title="Average KE",
    ymin=0.0,
    ymax=5.0,
    xmin=0,
    xmax=500,
    xtitle="time",
    ytitle="KE avg",
)
Kavegraph = gcurve(color=color.red)
sceneT = graph(
    x=0,
    y=500,
    width=600,
    height=150,
    title="Average PE",
    ymin=-60,
    ymax=0.0,
    xmin=0,
    xmax=500,
    xtitle="time",
    ytitle="PE avg",
)
Tcurve = gcurve(color=color.cyan)
Natom = 25
Nmax = 25
Tinit = 2.0
# Density (1.20 for fcc)
dens = 1.0
t1 = 0
x = np.zeros((Nmax), float)
y = np.zeros((Nmax), float)
vx = np.zeros((Nmax), float)
vy = np.zeros((Nmax), float)
fx = np.zeros((Nmax, 2), float)
fy = np.zeros((Nmax, 2), float)
# Side of lattice
L = int(1.0 * Natom**0.5)
atoms = []


# Average 12 rands for Gaussian
def twelveran():
    s = 0.0
    for i in range(1, 13):
        s += random.random()
    return s / 12.0 - 0.5


# Initialize
def initialposvel():
    i = -1
    # x->   0  1  2  3  4
    for ix in range(0, L):
        # y=0   0  5  10 15 20
        for iy in range(0, L):
            # y=1   1  6  11 16 21
            i = i + 1
            # y=2   2  7  12 17 22
            x[i] = ix
            # y=3   3  8  13 18 23
            y[i] = iy
            # y=4   4  9  14 19 24
            vx[i] = twelveran()
            # numbering of 25 atoms
            vy[i] = twelveran()
            vx[i] = vx[i] * sqrt(Tinit)
            vy[i] = vy[i] * sqrt(Tinit)
    for j in range(0, Natom):
        xc = 2 * x[j] - 4
        yc = 2 * y[j] - 4
        atoms.append(sphere(pos=vector(xc, yc, 0), radius=0.5, color=color.red))


def sign(a, b):
    if b >= 0.0:
        return abs(a)
    else:
        return -abs(a)


# Forces
def Forces(t, w, PE, PEorW):
    # invr2 = 0.
    # Switch: PEorW = 1 for PE
    r2cut = 9.0
    PE = 0.0
    for i in range(0, Natom):
        fx[i][t] = fy[i][t] = 0.0
    for i in range(0, Natom - 1):
        for j in range(i + 1, Natom):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if abs(dx) > 0.50 * L:
                # Closest image
                dx = dx - sign(L, dx)
            if abs(dy) > 0.50 * L:
                dy = dy - sign(L, dy)
            r2 = dx * dx + dy * dy
            if r2 < r2cut:
                # To avoid 0 denominator
                if r2 == 0.0:
                    r2 = 0.0001
                invr2 = 1.0 / r2
                wij = 48.0 * (invr2**3 - 0.5) * invr2**3
                fijx = wij * invr2 * dx
                fijy = wij * invr2 * dy
                fx[i][t] = fx[i][t] + fijx
                fy[i][t] = fy[i][t] + fijy
                fx[j][t] = fx[j][t] - fijx
                fy[j][t] = fy[j][t] - fijy
                PE = PE + 4.0 * (invr2**3) * ((invr2**3) - 1.0)
                w = w + wij
    if PEorW == 1:
        return PE
    else:
        return w


def timevolution():
    avT = 0.0
    avP = 0.0
    Pavg = 0.0
    avKE = 0.0
    avPE = 0.0
    t1 = 0
    PE = 0.0
    # step
    h = 0.031
    hover2 = h / 2.0
    # initial KE & PE via Forces
    KE = 0.0
    w = 0.0
    initialposvel()
    for i in range(0, Natom):
        KE = KE + (vx[i] * vx[i] + vy[i] * vy[i]) / 2
    PE = Forces(t1, w, PE, 1)
    time = 1
    while 1:
        rate(100)
        for i in range(0, Natom):
            PE = Forces(t1, w, PE, 1)
            x[i] = x[i] + h * (vx[i] + hover2 * fx[i][t1])
            y[i] = y[i] + h * (vy[i] + hover2 * fy[i][t1])
            if x[i] <= 0.0:
                # Periodic BC
                x[i] = x[i] + L
            if x[i] >= L:
                x[i] = x[i] - L
            if y[i] <= 0.0:
                y[i] = y[i] + L
            if y[i] >= L:
                y[i] = y[i] - L
            xc = 2 * x[i] - 4
            yc = 2 * y[i] - 4
            atoms[i].pos = vector(xc, yc, 0)
        PE = 0.0
        t2 = 1
        PE = Forces(t2, w, PE, 1)
        KE = 0.0
        w = 0.0
        for i in range(0, Natom):
            vx[i] = vx[i] + hover2 * (fx[i][t1] + fx[i][t2])
            vy[i] = vy[i] + hover2 * (fy[i][t1] + fy[i][t2])
            KE = KE + (vx[i] * vx[i] + vy[i] * vy[i]) / 2
        w = Forces(t2, w, PE, 2)
        P = dens * (KE + w)
        # increment averages
        T = KE / (Natom)
        avT = avT + T
        avP = avP + P
        avKE = avKE + KE
        avPE = avPE + PE
        time += 1
        t = time
        if t == 0:
            t = 1
        Pavg = avP / t
        eKavg = avKE / t
        ePavg = avPE / t
        Tavg = avT / t
        pre = (int)(Pavg * 1000)
        Pavg = pre / 1000.0
        kener = (int)(eKavg * 1000)
        eKavg = kener / 1000.0
        Kavegraph.plot(pos=(t, eKavg))
        pener = (int)(ePavg * 1000)
        ePavg = pener / 1000.0
        tempe = (int)(Tavg * 1000000)
        Tavg = tempe / 1000000.0
        Tcurve.plot(pos=(t, ePavg), canvas=sceneT)


timevolution()
