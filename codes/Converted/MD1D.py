""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# MD1.py          Molecular dynamics in 1D

from visual import *
from visual.graph import *
import random

# Spheres
scene = canvas( x=0, y=0, width=700, height=350, title="Molecular Dynamics", range=12 )  
sceneK = graph( x=0, y=350, width=600, height=150, title="Average KE", ymin=0.0, ymax=0.3, xmin=0, xmax=100, xtitle="time", ytitle="KE avg", )
# plot KE
Kavegraph = gcurve(color=color.red)  
scenePE = graph( x=0, y=500, width=600, height=150, title="Pot Energy", ymin=-0.6, ymax=0.0, xmin=0, xmax=100, xtitle="time", ytitle="PE", )
PEcurve = gcurve(color=color.cyan)
Natom = 8
Nmax = 8
# T initial
Tinit = 10.0  
t1 = 0
x = zeros((Nmax), float)
vx = zeros((Nmax), float)
fx = zeros((Nmax, 2), float)
# Length of atom chain
L = Natom  
atoms = []


# Gaussian as average 12 randoms
def twelveran():  
    s = 0.0
    for i in range(1, 13):
        s += random.random()
    return s / 12.0 - 0.5


# Initial positions, velocities
def initialposvel():  
    i = -1
    for ix in range(0, L):
        i = i + 1
        x[i] = ix
        vx[i] = twelveran()
        vx[i] = vx[i] * sqrt(Tinit)
    for j in range(0, Natom):
# Linear transform to place spheres
        xc = 2 * x[j] - 7  
        atoms.append(sphere(pos=vector(xc, 0,0), radius=0.5, color=color.red))


def sign(a, b):
    if b >= 0.0:
        return abs(a)
    else:
        return -abs(a)


# Forces
def Forces(t, PE):  
# Cutoff
    r2cut = 9.0  
    PE = 0.0
    for i in range(0, Natom):
        fx[i][t] = 0.0
    for i in range(0, Natom - 1):
        for j in range(i + 1, Natom):
            dx = x[i] - x[j]
            if abs(dx) > 0.50 * L:
# Interact closest image
                dx = dx - sign(L, dx)  
            r2 = dx * dx
            if r2 < r2cut:
# Avoid 0 denominator
                if r2 == 0.0:  
                    r2 = 0.0001
                invr2 = 1.0 / r2
                wij = 48.0 * (invr2**3 - 0.5) * invr2**3
                fijx = wij * invr2 * dx
                fx[i][t] = fx[i][t] + fijx
                fx[j][t] = fx[j][t] - fijx
                PE = PE + 4.0 * (invr2**3) * ((invr2**3) - 1.0)
    return PE


def timevolution():
    t1 = 0
    t2 = 1
# Unstable if larger
    h = 0.038  
    hover2 = h / 2.0
    KE = 0.0
    PE = 0.0
    initialposvel()
    PE = Forces(t1, PE)
# Kinetic energy
    for i in range(0, Natom):  
        KE = KE + (vx[i] * vx[i]) / 2.0
    t = 0
# Time loop
    while t < 100:  
        rate(1)
        for i in range(0, Natom):
            PE = Forces(t1, PE)
            x[i] = x[i] + h * (vx[i] + hover2 * fx[i][t1])
            if x[i] <= 0.0:
# Periodic bBC
                x[i] = x[i] + L  
            if x[i] >= L:
                x[i] = x[i] - L
# Linear transform
            xc = 2 * x[i] - 8  
            atoms[i].pos = vector(xc, 0,0)
        PE = 0.0
        PE = Forces(t2, PE)
        KE = 0.0
        for i in range(0, Natom):
            vx[i] = vx[i] + hover2 * (fx[i][t1] + fx[i][t2])
            KE = KE + (vx[i] * vx[i]) / 2
        T = 2 * KE / (3 * Natom)
        Itemp = t1
        t1 = t2
        t2 = Itemp
# Plot KE
        Kavegraph.plot(pos=(t, KE))  
# Plot PE
        PEcurve.plot(pos=(t, PE), canvas=scenePE)  
        t += 1


timevolution()
