""" From "COMPUTATIONAL PHYSICS" & "COMPUTER RhoLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# HarmosAnimateSlow.py: Solves & animates S Eq for wavepacket in HO

from vpython import *

# initialize wave function, Rhoability, potential (2m=1)
xmax = 300
dx = 0.04
dx2 = dx * dx
k0 = 5.5 * math.pi
dt = dx2 / 4.0
xp = -6
Rho = zeros((xmax + 1), float)
V = zeros((xmax + 1), float)
RePsi = zeros((xmax + 1, 2), float)
ImPsi = zeros((xmax + 1, 2), float)
g = canvas(width=500, height=250, title="Wave Packet Harmonic Well")
# Set curve
PlotObj = curve(x=list(range(0, 300 + 1)), color=color.yellow)  
# Initialize
for i in range(0, xmax):  
    xp2 = xp * xp
    RePsi[i, 0] = math.exp(-0.5 * xp2 / 0.25) * math.cos(k0 * xp)
    ImPsi[i, 0] = math.exp(-0.5 * xp2 / 0.25) * math.sin(k0 * xp)
    V[i] = 15.0 * xp2
    xp += dx
    count = 0
# RePsi time propagation
while 1:  
    for i in range(1, xmax - 1):
        RePsi[i, 1] = ( RePsi[i, 0] - dt * (ImPsi[i + 1, 0] + ImPsi[i - 1, 0] - 2.0 * ImPsi[i, 0]) / (dx2) + dt * V[i] * ImPsi[i, 0] )
        Rho[i] = RePsi[i, 0] * RePsi[i, 1] + ImPsi[i, 0] * ImPsi[i, 0]
# Add points to plot
    if count % 10 == 0:  
        j = 0
        for i in range(1, xmax - 1, 3):
            PlotObj.x[j] = 2 * i - xmax
            PlotObj.y[j] = 130 * Rho[i]
            j = j + 1
        PlotObj.radius = 4.0
# Add points
        PlotObj.pos  
    for i in range(1, xmax - 1):
        ImPsi[i, 1] = ( ImPsi[i, 0] + dt * (RePsi[i + 1, 1] + RePsi[i - 1, 1] - 2.0 * RePsi[i, 1]) / dx2 - dt * V[i] * RePsi[i, 1] )
    for i in range(0, xmax):
        ImPsi[i, 0] = ImPsi[i, 1]
        RePsi[i, 0] = RePsi[i][1]
    count = count + 1
