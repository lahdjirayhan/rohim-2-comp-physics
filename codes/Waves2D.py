""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Waves2D.py: Helmholtz eqn for rectangular membrane

import matplotlib.pylab as p
from numpy import *
from mpl_toolkits.mplot3d import Axes3D

"""Init condtns: u(x,y,t=0)=0 at borders, du/dt(x,y,t=0)=0                       
    Tension = 180 N/m^2, density = 390.0 kg/m^2 (rubber)"""

tim = 15
N = 71
# Speed = sqrt(ten[]/den[kg/m2;])
c = sqrt(180.0 / 390)  
u = zeros((N, N, N), float)
v = zeros((N, N), float)
incrx = pi / N
incry = pi / N
cprime = c
covercp = c / cprime
# c/c' 0.5 for stable
ratio = 0.5 * covercp * covercp  


def vibration(tim):
    y = 0.0
# Initial position
    for j in range(0, N):  
        x = 0.0
        for i in range(0, N):
# Initial shape
            u[i][j][0] = 3 * sin(2.0 * x) * sin(y)  
            x += incrx
        y += incry

# First time step
    for j in range(1, N - 1):  
        for i in range(1, N - 1):
            u[i][j][1] = u[i][j][0] + 0.5 * ratio * ( u[i + 1][j][0] + u[i - 1][j][0] + u[i][j + 1][0] + u[i][j - 1][0] - 4.0 * u[i][j][0] )

# Later time steps
    for k in range(1, tim):  
        for j in range(1, N - 1):
            for i in range(1, N - 1):
                u[i][j][2] = ( 2.0 * u[i][j][1] - u[i][j][0] + ratio * ( u[i + 1][j][1] + u[i - 1][j][1] + u[i][j + 1][1] + u[i][j - 1][1] - 4.0 * u[i][j][1] ) )
# Reset past
        u[:][:][0] = u[:][:][1]  
# Reset present
        u[:][:][1] = u[:][:][2]  
        for j in range(0, N):
            for i in range(0, N):
# Convert to 2D for matplotlib
                v[i][j] = u[i][j][2]  
    return v


v = vibration(tim)
x1 = list(range(0, N))
y1 = list(range(0, N))
X, Y = p.meshgrid(x1, y1)


def functz(v):
    z = v[X, Y]
    return z


Z = functz(v)
fig = p.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color="r")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("u(x,y)")
p.show()
