""" From  "COMPUTER PROBLEMS in PHYSICS"  by RH Landau & MJ Paez
    Copyright R Landau,   MJ Paez,    2017. 
    Please respect copyright & acknowledge our work."""


# TwoWells.py:  Time-dependent Schroedinger packets in two wells

from vpython import *

dx = 0.08
dx2 = dx * dx
k0 = 5.0
dt = dx2 / 8
Nmax = 200
addi = 250

V_L = zeros((Nmax), float)
V_R = zeros((Nmax), float)
V2 = zeros((Nmax + addi), float)
RePsiL = zeros((Nmax + 1), float)
ImPsiL = zeros((Nmax + 1), float)
Rho = zeros((Nmax + 1), float)
RhoR = zeros((Nmax + 1), float)
RePsiR = zeros((Nmax + 1), float)
ImPsiR = zeros((Nmax + 1), float)
RePsi2L = zeros((Nmax + addi), float)
ImPsi2L = zeros((Nmax + addi), float)
RhoAL = zeros((Nmax + addi), float)
Rho2R = zeros((Nmax + addi), float)
RePsi2R = zeros((Nmax + addi), float)
Psi2R = zeros((Nmax + addi), float)
Xleft = arange(-18.0, -2.0, 0.08)
Xright = arange(2.0, 18.0, 0.08)
Xall = arange(-18, 18, 0.08)

g = canvas(width=500, height=500)
g.center = vector(0, 0, 20)
cL = curve(color=color.red, x=Xleft)
cR = curve(color=color.yellow, x=Xright)
# Vert line tru x=0
curve(pos=[(0, 250), (0, -250)])  
PlotObj = curve(x=Xleft, color=color.red, radius=0.8)
PlotObjR = curve(x=Xleft, color=color.yellow, radius=0.8)
escena2 = canvas(width=500, height=500, x=500)
allc = curve(color=color.green, x=Xall)
# Vertical line tru x=0
curve(pos=[(0, 250), (0, -250)])  
PlotAllR = curve(x=Xall, color=color.cyan, radius=0.8, canvas=escena2)


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
    cL.x = 10 * Xleft + 15
# Widen
    cR.x = 10 * Xright - 15  
    cL.y = 10 * (Xleft + 10) ** 2 / 2 - 100
    cR.y = 10 * (Xright - 10) ** 2 / 2 - 100
    allc.x = 8 * Xall
    allc.y = V2 - 100
    i = i + 1


plotpotentials()
# Initial psi
RePsiL = exp(-5 * ((Xleft + 10)) ** 2) * cos(k0 * Xleft)  
ImPsiL = exp(-5 * ((Xleft + 10)) ** 2) * sin(k0 * Xleft)
Rho = RePsiL * RePsiL + ImPsiL * ImPsiL
# Just On side
RePsiR = exp(-5 * ((Xright - 10)) ** 2) * cos(-k0 * Xright)  
ImPsiR = exp(-5 * ((Xright - 10)) ** 2) * sin(-k0 * Xright)
RhoR = RePsiR**2 + ImPsiR**2
# initial conditions
for i in range(0, 450):  
# gives -18 <=x <=18
    x = -18 + i * dx  
    if i <= 225:
# to middle
        RePsi2L[i] = 0 * exp(-5 * (x + 10) ** 2) * cos(k0 * x)  
        ImPsi2L[i] = 0 * exp(-5 * (x + 10) ** 2) * sin(k0 * x)
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
        RePsi2R[j] = exp(-5 * (x - 10) ** 2) * cos(-k0 * x)  
        Psi2R[j] = exp(-5 * (x - 10) ** 2) * sin(-k0 * x)
    Rho2R[j] = 50.0 * (RePsi2R[j] ** 2 + Psi2R[j] ** 2)
for t in range(0, 2900):
    rate(100)
    RePsiL[1:-1] = ( RePsiL[1:-1] - (dt / dx2) * (ImPsiL[2:] + ImPsiL[:-2] - 2 * ImPsiL[1:-1]) + dt * V_L[1:-1] * ImPsiL[1:-1] )
    ImPsiL[1:-1] = ( ImPsiL[1:-1] + (dt / dx2) * (RePsiL[2:] + RePsiL[:-2] - 2 * RePsiL[1:-1]) - dt * V_L[1:-1] * RePsiL[1:-1] )
# RHS left figure
    PlotObj.x = 10 * (Xleft) + 15  
    PlotObj.y = 50 * (RePsiL**2 + ImPsiL**2) + 150
    RePsiR[1:-1] = ( RePsiR[1:-1] - (dt / dx2) * (ImPsiR[2:] + ImPsiR[:-2] - 2 * ImPsiR[1:-1]) + dt * V_R[1:-1] * ImPsiR[1:-1] )
    ImPsiR[1:-1] = ( ImPsiR[1:-1] + (dt / dx2) * (RePsiR[2:] + RePsiR[:-2] - 2 * RePsiR[1:-1]) - dt * V_R[1:-1] * RePsiR[1:-1] )
# LHS left figure
    PlotObjR.x = 10 * (Xright) - 15  
    PlotObjR.y = 50 * (RePsiR**2 + ImPsiR**2) + 150
    RePsi2L[1:-1] = ( RePsi2L[1:-1] - (dt / dx2) * (ImPsi2L[2:] + ImPsi2L[:-2] - 2 * ImPsi2L[1:-1]) + dt * V2[1:-1] * ImPsi2L[1:-1] )
    ImPsi2L[1:-1] = ( ImPsi2L[1:-1] + (dt / dx2) * (RePsi2L[2:] + RePsi2L[:-2] - 2 * RePsi2L[1:-1]) - dt * V2[1:-1] * RePsi2L[1:-1] )
    RePsi2R[1:-1] = ( RePsi2R[1:-1] - (dt / dx2) * (Psi2R[2:] + Psi2R[:-2] - 2 * Psi2R[1:-1]) + dt * V2[1:-1] * Psi2R[1:-1] )
    Psi2R[1:-1] = ( Psi2R[1:-1] + (dt / dx2) * (RePsi2R[2:] + RePsi2R[:-2] - 2 * RePsi2R[1:-1]) - dt * V2[1:-1] * RePsi2R[1:-1] )
    PlotAllR.x = 8 * (Xall)
    PlotAllR.y = 70 * (RePsi2R**2 + Psi2R**2) + 150
    +50 * (RePsi2L**2 + ImPsi2L**2)
