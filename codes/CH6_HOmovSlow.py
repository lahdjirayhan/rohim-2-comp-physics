""" From "COMPUTATIONAL PHYSICS" & "COMPUTER RhoLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# HOmovieSlow.py: Solves & animates S Eq for wavepacket in HO

from vpython import *
import numpy as np

# initialize wave function, Rhoability, potential (2m=1)
xmax = 300
dx = 0.04
dx2 = dx * dx
k0 = 5.5 * np.pi
dt = dx2 / 4.0
xp = -6
Rho = np.zeros((xmax + 1), float)
V = np.zeros((xmax + 1), float)
RePsi = np.zeros((xmax + 1, 2), float)
ImPsi = np.zeros((xmax + 1, 2), float)
g = canvas(width=500, height=250, title="Wave Packet Harmonic Well")
PlotObj = curve(
    pos=[(x, 0, 0) for x in range(0, xmax + 1)], color=color.yellow, radius=4
)
# Initialize
for i in range(0, xmax):
    xp2 = xp * xp
    RePsi[i, 0] = np.exp(-0.5 * xp2 / 0.25) * np.cos(k0 * xp)
    ImPsi[i, 0] = np.exp(-0.5 * xp2 / 0.25) * np.sin(k0 * xp)
    V[i] = 15.0 * xp2
    xp += dx
    count = 0
# RePsi time propagation
while True:
    for i in range(1, xmax - 1):
        RePsi[i, 1] = (
            RePsi[i, 0]
            - dt * (ImPsi[i + 1, 0] + ImPsi[i - 1, 0] - 2.0 * ImPsi[i, 0]) / (dx2)
            + dt * V[i] * ImPsi[i, 0]
        )
        Rho[i] = RePsi[i, 0] * RePsi[i, 1] + ImPsi[i, 0] * ImPsi[i, 0]
    # Add points to plot
    if count % 10 == 0:
        j = 0
        for i in range(1, xmax - 1):
            PlotObj_x_j = 2 * i - xmax
            PlotObj_y_j = 130 * Rho[i]
            PlotObj.modify(j, x=PlotObj_x_j, y=PlotObj_y_j)
            j += 1
    for i in range(1, xmax - 1):
        ImPsi[i, 1] = (
            ImPsi[i, 0]
            + dt * (RePsi[i + 1, 1] + RePsi[i - 1, 1] - 2.0 * RePsi[i, 1]) / dx2
            - dt * V[i] * RePsi[i, 1]
        )
    for i in range(0, xmax):
        ImPsi[i, 0] = ImPsi[i, 1]
        RePsi[i, 0] = RePsi[i, 1]
    count = count + 1
