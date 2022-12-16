""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Torricelli.py: solves Navier-Stokes equation for orifice flow

# Need for zeros
from numpy import *  

Niter = 700
Ndown = 20
Nx = 17
N2x = 2 * Nx
Ny = 156
Nb = 15
h = 0.4
h2 = h * h
g = 980.0
nu = 0.5
iter = 0
Vtop = 8.0e-4
omega = 0.1
R = Vtop * h / nu

u = zeros((Nx + 1, Ny + 1), float)
ua = zeros((N2x, Ny), float)
w = zeros((Nx + 1, Ny + 1), float)

Torri = open("Torri.dat", "w")
uall = open("uall.dat", "w")


def BelowHole():
# Below orifice
    for i in range(Nb + 1, Nx + 1):  
# du/dy =vx=0
        u[i, 0] = u[i - 1, 1]  
# Water is at floor
        w[i - 1, 0] = w[i - 1, 1]  
        for j in range(0, Ndown + 1):
            if i == Nb:
                vy = 0
            if i == Nx:
                vy = -sqrt(2.0 * g * h * (Ny + Nb - j))
            if i == Nx - 1:
                vy = -sqrt(2.0 * g * h * (Ny + Nb - j)) / 2.0
# du/dx=-vy
            u[i, j] = u[i - 1, j] - vy * h  


def BorderRight():
# Center orifice very sensitive
    for j in range(1, Ny + 1):  
        vy = -sqrt(2.0 * g * h * (Ny - j))
        u[Nx, j] = u[Nx - 1, j] + vy * h
        u[Nx, j] = u[Nx, j - 1]
        w[Nx, j] = -2 * (u[Nx, j] - u[Nx, j - 1]) / h**2


def BottomBefore():
# Bottom,  before the hole
    for i in range(1, Nb + 1):  
        u[i, Ndown] = u[i, Ndown - 1]
        w[i, Ndown] = -2 * (u[i, 0] - u[i, 1])


def Top():
# Top
    for i in range(1, Nx):  
        u[i, Ny] = u[i, Ny - 1]
        w[i, Ny] = 0


def Left():
# Left wall
    for j in range(Ndown, Ny):  
        w[0, j] = -2 * (u[0, j] - u[1, j]) / h**2
# du/dx=0
        u[0, j] = u[1, j]  


# Method borders: init & B.C.
def Borders(iter):  
    BelowHole()
# right (center of hole)
    BorderRight()  
# Bottom before the hole
    BottomBefore()  
    Top()
    Left()


def Relax(iter):
    Borders(iter)
    for i in range(1, Nx):
        for j in range(1, Ny):
            if j <= Ndown:
                if i > Nb:
                    r1 = omega * ( ( u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1] + h * h * w[i, j] ) * 0.25 - u[i, j] )
                    u[i, j] += r1
            if j > Ndown:
                r1 = omega * ( ( u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1] + h * h * w[i, j] ) * 0.25 - u[i, j] )
                u[i, j] += r1
    if iter % 50 == 0:
        print(("Residual r1 ", r1))
    Borders(iter)
# Relax stream function
    for i in range(1, Nx):  
        for j in range(1, Ny):
            if j <= Ndown:
                if i >= Nb:
                    a1 = w[i + 1, j] + w[i - 1, j] + w[i, j + 1] + w[i, j - 1]
                    a2 = vector(u[i, j + 1] - u[i, j - 1]) * (w[i + 1, j] - w[i - 1, j])
                    a3 = vector(u[i + 1, j] - u[i - 1, j]) * (w[i, j + 1] - w[i, j - 1])
                    r2 = omega * ((a1 + (R / 4.0) * (a3 - a2)) / 4.0 - w[i, j])
                    w[i, j] += r2
            if j > Ndown:
                a1 = w[i + 1, j] + w[i - 1, j] + w[i, j + 1] + w[i, j - 1]
                a2 = vector(u[i, j + 1] - u[i, j - 1]) * (w[i + 1, j] - w[i - 1, j])
                a3 = vector(u[i + 1, j] - u[i - 1, j]) * (w[i, j + 1] - w[i, j - 1])
                r2 = omega * ((a1 + (R / 4.0) * (a3 - a2)) / 4.0 - w[i, j])
                w[i, j] += r2


while iter <= Niter:
    if iter % 100 == 0:
# iterations counted
        print(("Iteration", iter))  
    Relax(iter)
# counter of iterations
    iter += 1  
# Send w to disk in gnuplot format
for j in range(0, Ny):  
    for i in range(0, Nx):
        Torri.write("%8.3e \n" % (w[i, j]))
    Torri.write("\n")
Torri.close()
# Send symmetric tank data to disk
for j in range(0, Ny):  
    for i in range(0, N2x):
        if i <= Nx:
            ua[i, j] = u[i, j]
            uall.write("%8.3e \n" % (ua[i, j]))
        if i > Nx:
            ua[i, j] = u[N2x - i, j]
            uall.write("%8.3e \n" % (ua[i, j]))
    uall.write("\n")
uall.close()
# Send u data to disk
utorr = open("Torri.dat", "w")  
for j in range(0, Ny):
    utorr.write("\n")
    for i in range(0, Nx):
        utorr.write("%10.3e  \n" % (u[i, j]))
utorr.close()
