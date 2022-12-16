""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# 3QMdisksVis.py: Wavepacket scattering from 3 disks wi Visual

from visual import *

R = 24
N = 101
dx = 0.1
k0 = 20.0
# (90.*sqrt3/2-30)
x1 = 51  
k1 = 0.0
dt = 0.002
dx2 = dx * dx
fc = dt / dx2
Xo = -50
Yo = 24
V = zeros((N, N), float)
RePsi = zeros((N, N), float)
ImPsi = zeros((N, N), float)


# Potential three disk
def Pot3Disk():  
    Pot1Disk(-30, 45)
    Pot1Disk(-30, -45)
    Pot1Disk(x1, 0)


# Potential single disk
def Pot1Disk(xa, ya):  
    for y in range(ya - R, ya + R + 1):
        for x in range(xa - R, xa + R + 1):
            if sqrt((x - xa) ** 2 + (y - ya) ** 2) <= R:
                i = int(50.0 / 100.0 * y + 50)
                j = int(50.0 / 100.0 * x + 50)
# A very high pot
                V[i, j] = 5.0  


# Psi_0 wave packet
def Psi_0(Xo, Yo):  
    for i in arange(0, N):
        y = 200.0 / 100.0 * i - 100
        for j in arange(0, N):
            x = 200.0 / 100.0 * j - 100
            Gaussian = exp(-0.01 * (x - Xo) ** 2 - 0.01 * (y - Yo) ** 2)
            RePsi[i, j] = Gaussian * cos(k0 * x + k1 * y)
            ImPsi[i, j] = Gaussian * sin(k0 * x + k1 * y)


def PlotPsi_0():
    for i in range(1, N - 1):
        yp = 200.0 * i / N - 100
        for j in range(1, N - 1):
            if V[i, j] != 0:
                RePsi[i, j] = ImPsi[i, j] = 0
            Rho = 40 * (RePsi[i, j] ** 2 + ImPsi[i, j] ** 2)
# To avoid long lines
            if Rho > 0.01:  
                xx = 200.0 * j / N - 100.0
                xm1 = 200.0 * (j - 1) / N - 100.0
                Rhom1 = 40 * (RePsi[i, j - 1] ** 2 + ImPsi[i, j - 1] ** 2)
# Plot segment of 40*Psi
                yy = yp  
                curve(pos=[(xm1, Rhom1, yy), (xx, Rho, yy)], color=color.red)


scene = canvas( width=500, height=500, range=120, background=color.white, foreground=color.black )
table = curve( pos=( [ (-100, 0, -100), (100, 0, -100), (100, 0, 100), (-100, 0, 100), (-100, 0, -100), ] ) )
circ1 = ring(pos=vector(-30, 0, 45), radius=R, axis=vector(0, 1, 0), color=color.blue)
circ2 = ring(pos=vector(-30, 0, -45), radius=R, axis=vector(0, 1, 0), color=color.blue)
circ3 = ring(pos=vector(x1, 0, 0), radius=R, axis=vector(0, 1, 0), color=color.blue)
# Scene's angle of vision
scene.forward = vector(0, -1, -1)  
Pot3Disk()
Psi_0(Xo, Yo)

PlotPsi_0()
# Plot every 10 t's
for t in range(0, 150):  
    if t % 10 == 0:
        print(("time =", t))
    ImPsi[1:-1, 1:-1] = ( ImPsi[1:-1, 1:-1] + fc * ( RePsi[2:, 1:-1] + RePsi[:-2, 1:-1] - 4 * RePsi[1:-1, 1:-1] + RePsi[1:-1, 2:] + RePsi[1:-1, :-2] ) + V[1:-1, 1:-1] * dt * RePsi[1:-1, 1:-1] )
    RePsi[1:-1, 1:-1] = ( RePsi[1:-1, 1:-1] - fc * ( ImPsi[2:, 1:-1] + ImPsi[:-2, 1:-1] - 4 * ImPsi[1:-1, 1:-1] + ImPsi[1:-1, 2:] + ImPsi[1:-1, :-2] ) + V[1:-1, 1:-1] * dt * ImPsi[1:-1, 1:-1] )
    for i in range(1, N - 1):
        yp = 200.0 * i / N - 100
        for j in range(1, N - 1):
            if V[i, j] != 0:
                RePsi[i, j] = ImPsi[i, j] = 0
            Rho = 40 * (RePsi[i, j] ** 2 + ImPsi[i, j] ** 2)
            xx = 200.0 * j / N - 100.0
            xm1 = 200.0 * (j - 1) / N - 100.0
            Rhom1 = 40 * (RePsi[i, j - 1] ** 2 + ImPsi[i, j - 1] ** 2)
            yy = yp
            if Rho > 0.1:
                if t % 10 == 0:
                    curve(pos=[(xm1, Rhom1, yy), (xx, Rho, yy)], color=color.red)
print("finito")
