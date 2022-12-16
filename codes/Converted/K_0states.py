""" From "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau &  MJ Paez, 
    Copyright R Landau, MJ Paez, 2017. 
    Please respect copyright & acknowledge our work."""

# K_0states.py: Wavepacket in double well

from visual.graph import *

dx = 0.04
dx2 = dx * dx
k0 = 0.3
dt = dx2 / 18.0
Xmax = 8.0
nmax = int(2 * Xmax / dx)
X = arange(-Xmax, Xmax, dx)
Rho = zeros((nmax + 1), float)
V = zeros((nmax + 2), float)
p2 = zeros((nmax + 1), float)
RePsi = zeros((nmax + 1), float)
ImPsi = zeros((nmax + 1), float)

g = canvas( width=1200, height=1500, title="Wave Packet in Double Well", background=color.white, foreground=color.black, )
# Packet
PlotObj = curve(x=X, color=color.red, radius=0.02)  
# Potential
Potential = curve(x=X, color=color.black, radius=0.02)  
RHL = exp(-5.5 * ((X + 4.5)) ** 2)
RePsi = RHL * cos(k0 * X)
# Initial Psi
ImPsi = RHL * sin(k0 * X)  
Rho = RePsi * RePsi + ImPsi * ImPsi

i = 0
# Left side V
for x in arange(-Xmax + 1, 0, dx):  
    i = i + 1
    V[i] = 20 * (x + 3.0) ** 2
# Right side V
for x in arange(0, Xmax + 1, dx):  
    V[i] = 20 * (x - 3.0) ** 2
    i = i + 1

j = 0
for x in arange(-Xmax, Xmax, dx):
    PlotObj.x[j] = x
# Scaled to fit
    PlotObj.y[j] = 5 * Rho[j] - 2  
    Potential.x[j] = x
# Scaled to fit
    Potential.y[j] = 0.03 * V[j]  
    j = j + 1

# Time stepping
for t in range(0, 15000):  
    rate(900)
    for i in range(1, nmax - 1):
        RePsi[i] = ( RePsi[i] - dt * (ImPsi[i + 1] + ImPsi[i - 1] - 2.0 * ImPsi[i]) / (dx * dx) + dt * V[i] * ImPsi[i] )
        p2[i] = RePsi[i] * RePsi[i] + ImPsi[i] * ImPsi[i]
    for i in range(1, nmax - 1):
        ImPsi[i] = ( ImPsi[i] + dt * (RePsi[i + 1] + RePsi[i - 1] - 2.0 * RePsi[i]) / (dx * dx) - dt * V[i] * RePsi[i] )
# Scaled rho
    PlotObj.y = 10 * (RePsi**2 + ImPsi**2)  
