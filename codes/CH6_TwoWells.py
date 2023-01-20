""" From  "COMPUTER PROBLEMS in PHYSICS"  by RH Landau & MJ Paez
    Copyright R Landau,   MJ Paez,    2017.
    Please respect copyright & acknowledge our work."""


# TwoWells.py:  Time-dependent Schroedinger packets in two wells

from vpython import *
import numpy as np

dx = 0.08
dx2 = dx * dx
k0 = 5.0
dt = dx2 / 8
Nmax = 200
addi = 250

V_L = np.zeros((Nmax), float)
V_R = np.zeros((Nmax), float)
V2 = np.zeros((Nmax + addi), float)
RePsiL = np.zeros((Nmax + 1), float)
ImPsiL = np.zeros((Nmax + 1), float)
Rho = np.zeros((Nmax + 1), float)
RhoR = np.zeros((Nmax + 1), float)
RePsiR = np.zeros((Nmax + 1), float)
ImPsiR = np.zeros((Nmax + 1), float)
RePsi2L = np.zeros((Nmax + addi), float)
ImPsi2L = np.zeros((Nmax + addi), float)
RhoAL = np.zeros((Nmax + addi), float)
Rho2R = np.zeros((Nmax + addi), float)
RePsi2R = np.zeros((Nmax + addi), float)
Psi2R = np.zeros((Nmax + addi), float)
Xleft = arange(-18.0, -2.0, 0.08)
Xright = arange(2.0, 18.0, 0.08)
Xall = arange(-18, 18, 0.08)

g = canvas(width=500, height=500)
g.center = vector(0, 0, 20)
cL = curve(pos=[(x, 0, 0) for x in Xleft], color=color.red, x=Xleft)
cR = curve(pos=[(x, 0, 0) for x in Xright], color=color.yellow, x=Xright)
# Vert line tru x=0
curve(pos=[(0, 250, 0), (0, -250, 0)])
PlotObj = curve(pos=[(x, 0, 0) for x in Xleft], color=color.red, radius=0.8)
PlotObjR = curve(pos=[(x, 0, 0) for x in Xright], color=color.yellow, radius=0.8)
escena2 = canvas(width=500, height=500, x=500)
allc = curve(color=color.green, pos=[(x, 0, 0) for x in Xall])
# Vertical line tru x=0
curve(pos=[(0, 250, 0), (0, -250, 0)])
PlotAllR = curve(
    pos=[(x, 0, 0) for x in Xall], color=color.cyan, radius=0.8, canvas=escena2
)


def potentials():
    for i in range(0, Nmax):
        # left well, left figure
        xL = -18.0 + i * dx
        V_L[i] = 10 * (xL + 10) ** 2 / 2
        xR = 2.0 + i * dx
        # right well left figure
        V_R[i] = 10 * (xR - 10) ** 2 / 2
    for j in range(0, Nmax + addi):
        xL = -18 + j * dx
        if j <= 125:
            # LHS
            V2[j] = 10.0 * (xL + 10) ** 2 / 2
        if j > 125 and j < 325:
            # Pert lowers
            V2[j] = V2[125]
        if j >= 325:
            # RHS right side
            V2[j] = 10.0 * (xL - 10) ** 2 / 2


potentials()


def plotpotentials(i=0):
    # Widen
    for i, x in enumerate(Xleft):
        cL.modify(i, x=10 * x + 15, y=10 * (x + 10) ** 2 / 2 - 100)

    for i, x in enumerate(Xright):
        cR.modify(i, x=10 * x - 15, y=10 * (x - 10) ** 2 / 2 - 100)

    for i, x in enumerate(Xall):
        allc.modify(i, x=8 * x, y=V2[i] - 100)

    i = i + 1


plotpotentials()
# Initial psi
RePsiL = np.exp(-5 * ((Xleft + 10)) ** 2) * np.cos(k0 * Xleft)
ImPsiL = np.exp(-5 * ((Xleft + 10)) ** 2) * np.sin(k0 * Xleft)
Rho = RePsiL * RePsiL + ImPsiL * ImPsiL
# Just On side
RePsiR = np.exp(-5 * ((Xright - 10)) ** 2) * np.cos(-k0 * Xright)
ImPsiR = np.exp(-5 * ((Xright - 10)) ** 2) * np.sin(-k0 * Xright)
RhoR = RePsiR**2 + ImPsiR**2
# initial conditions
for i in range(0, 450):
    # gives -18 <=x <=18
    x = -18 + i * dx
    if i <= 225:
        # to middle
        RePsi2L[i] = 0 * np.exp(-5 * (x + 10) ** 2) * np.cos(k0 * x)
        ImPsi2L[i] = 0 * np.exp(-5 * (x + 10) ** 2) * np.sin(k0 * x)
    # too small set=0
    else:
        RePsi2L[i] = 0.0
        ImPsi2L[i] = 0.0
    # Right psi
    RhoAL[i] = 50.0 * (RePsi2L[i] ** 2 + ImPsi2L[i] ** 2)
for j in range(0, 450):
    x = -18 + j * dx
    if j <= 225:
        # too smalll make it 0
        RePsi2R[j] = 0.0
        Psi2R[j] = 0.0
    else:
        # Left psi
        RePsi2R[j] = np.exp(-5 * (x - 10) ** 2) * np.cos(-k0 * x)
        Psi2R[j] = np.exp(-5 * (x - 10) ** 2) * np.sin(-k0 * x)
    Rho2R[j] = 50.0 * (RePsi2R[j] ** 2 + Psi2R[j] ** 2)
for t in range(0, 2900):
    rate(100)
    RePsiL[1:-1] = (
        RePsiL[1:-1]
        - (dt / dx2) * (ImPsiL[2:] + ImPsiL[:-2] - 2 * ImPsiL[1:-1])
        + dt * V_L[1:-1] * ImPsiL[1:-1]
    )
    ImPsiL[1:-1] = (
        ImPsiL[1:-1]
        + (dt / dx2) * (RePsiL[2:] + RePsiL[:-2] - 2 * RePsiL[1:-1])
        - dt * V_L[1:-1] * RePsiL[1:-1]
    )
    # RHS left figure
    for i, x in enumerate(Xleft):
        PlotObj.modify(i, x=10 * x + 15, y=50 * (RePsiL[i] ** 2 + ImPsiL[i] ** 2) + 150)

    RePsiR[1:-1] = (
        RePsiR[1:-1]
        - (dt / dx2) * (ImPsiR[2:] + ImPsiR[:-2] - 2 * ImPsiR[1:-1])
        + dt * V_R[1:-1] * ImPsiR[1:-1]
    )
    ImPsiR[1:-1] = (
        ImPsiR[1:-1]
        + (dt / dx2) * (RePsiR[2:] + RePsiR[:-2] - 2 * RePsiR[1:-1])
        - dt * V_R[1:-1] * RePsiR[1:-1]
    )
    # LHS left figure
    for i, x in enumerate(Xright):
        PlotObjR.modify(
            i, x=10 * x - 15, y=50 * (RePsiR[i] ** 2 + ImPsiR[i] ** 2) + 150
        )

    RePsi2L[1:-1] = (
        RePsi2L[1:-1]
        - (dt / dx2) * (ImPsi2L[2:] + ImPsi2L[:-2] - 2 * ImPsi2L[1:-1])
        + dt * V2[1:-1] * ImPsi2L[1:-1]
    )
    ImPsi2L[1:-1] = (
        ImPsi2L[1:-1]
        + (dt / dx2) * (RePsi2L[2:] + RePsi2L[:-2] - 2 * RePsi2L[1:-1])
        - dt * V2[1:-1] * RePsi2L[1:-1]
    )
    RePsi2R[1:-1] = (
        RePsi2R[1:-1]
        - (dt / dx2) * (Psi2R[2:] + Psi2R[:-2] - 2 * Psi2R[1:-1])
        + dt * V2[1:-1] * Psi2R[1:-1]
    )
    Psi2R[1:-1] = (
        Psi2R[1:-1]
        + (dt / dx2) * (RePsi2R[2:] + RePsi2R[:-2] - 2 * RePsi2R[1:-1])
        - dt * V2[1:-1] * RePsi2R[1:-1]
    )

    for i, x in enumerate(Xall):
        PlotAllR.modify(
            i,
            x=8 * x,
            y=70 * (RePsi2R[i] ** 2 + Psi2R[i] ** 2)
            + 150
            + 50 * (RePsi2L[i] ** 2 + ImPsi2L[i] ** 2),
        )
