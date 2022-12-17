""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# TwoDsol.java: solves Sine-Gordon equation for 2D soliton

from numpy import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np, matplotlib.pylab as plt, math

D = 201
dx = 14.0 / 200.0
dy = dx
dt = dx / sqrt(2.0)
dts = (dt / dx) * (dt / dx)

u = zeros((D, D, 3), float)
psi = zeros((D, D), float)


# initial conditions
def initial(u):
    yy = -7.0
    for i in range(0, D):
        xx = -7.0
        for j in range(0, D):
            tmp = 3.0 - sqrt(xx * xx + yy * yy)
            u[i][j][0] = 4.0 * (math.atan(tmp))
            xx = xx + dx
        yy = yy + dy


def solution(nint):
    time = 0.0
    for m in range(1, D - 1):
        for l in range(1, D - 1):
            a2 = u[m + 1][l][0] + u[m - 1][l][0] + u[m][l + 1][0] + u[m][l - 1][0]
            tmp = 0.25 * a2
            u[m][l][1] = 0.5 * (dts * a2 - dt * dt * sin(tmp))
    # Borders in second iteration
    for mm in range(1, D - 1):
        u[mm][0][1] = u[mm][1][1]
        u[mm][D - 1][1] = u[mm][D - 2][1]
        u[0][mm][1] = u[1][mm][1]
        u[D - 1][mm][1] = u[D - 2][mm][1]
    # Still undefined terms
    u[0][0][1] = u[1][0][1]
    u[D - 1][0][1] = u[D - 2][0][1]
    u[0][D - 1][1] = u[1][D - 1][1]
    u[D - 1][D - 1][1] = u[D - 2][D - 1][1]
    tmp = 0.0
    # Following iterations
    for k in range(0, nint + 1):
        print((k, "out of  ", nint))
        for m in range(1, D - 1):
            for l in range(1, D - 1):
                a1 = u[m + 1][l][1] + u[m - 1][l][1] + u[m][l + 1][1] + u[m][l - 1][1]
                tmp = 0.25 * a1
                u[m][l][2] = -u[m][l][0] + dts * a1 - dt * dt * sin(tmp)
                u[m][0][2] = u[m][1][2]
                u[m][D - 1][2] = u[m][D - 2][2]
        for mm in range(1, D - 1):
            u[mm][0][2] = u[mm][1][2]
            u[mm][D - 1][2] = u[mm][D - 2][2]
            u[0][mm][2] = u[1][mm][2]
            u[D - 1][mm][2] = u[D - 2][mm][2]
        u[0][0][2] = u[1][0][2]
        u[D - 1][0][2] = u[D - 2][0][2]
        u[0][D - 1][2] = u[1][D - 1][2]
        u[D - 1][D - 1][2] = u[D - 2][D - 1][2]
        # New iterations now old
        for l in range(0, D):
            for m in range(0, D):
                u[l][m][0] = u[l][m][1]
                u[l][m][1] = u[l][m][2]
        if k == nint:
            for i in range(0, D, 5):
                for j in range(0, D, 5):
                    psi[i][j] = sin(u[i][j][2] / 2)
        time = time + dt


def funcz(u):
    z = psi[X, Y]
    return z


initial(u)
time = 0.0
xx = arange(0, D, 5)
yy = arange(0, D, 5)
X, Y = plt.meshgrid(xx, yy)
# Number of time iterations
solution(22)
Z = funcz(psi)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_wireframe(X, Y, Z, color="g")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
print("Done")
