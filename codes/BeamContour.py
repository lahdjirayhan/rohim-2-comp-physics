""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Beam.py: solves Navier-Stokes equation for the flow around a beam

# Needed for range
from numpy import *  
import pylab as p
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import image

Nxmax = 70
Nymax = 20
# Grid parameters
# Stream
u = zeros((Nxmax + 1, Nymax + 1), float)  
# Vorticity
w = zeros((Nxmax + 1, Nymax + 1), float)  
# Initial v
V0 = 1.0  
# Relaxation param
omega = 0.1  
# Geometry
IL = 10  
H = 8
T = 8
h = 1.0
# Viscosity
nu = 1.0  
# Number iterations
iter = 0  
# Reynold number, normal units
R = V0 * h / nu  
print("Working, wait for the figure, count to 30")


# Initialize stream,vorticity, sets BC
def borders():  
# Initialize stream function
    for i in range(0, Nxmax + 1):  
# Init vorticity
        for j in range(0, Nymax + 1):  
            w[i, j] = 0.0
            u[i, j] = j * V0
# Fluid surface
    for i in range(0, Nxmax + 1):  
        u[i, Nymax] = u[i, Nymax - 1] + V0 * h
        w[i, Nymax - 1] = 0.0
    for j in range(0, Nymax + 1):
        u[1, j] = u[0, j]
# Inlet
        w[0, j] = 0.0  
# Centerline
    for i in range(0, Nxmax + 1):  
        if i <= IL and i >= IL + T:
            u[i, 0] = 0.0
            w[i, 0] = 0.0
# Outlet
    for j in range(1, Nymax):  
        w[Nxmax, j] = w[Nxmax - 1, j]
#  Borders
        u[Nxmax, j] = u[Nxmax - 1, j]  


# BC for the beam
def beam():  
# Beam sides
    for j in range(0, H + 1):  
# Front side
        w[IL, j] = -2 * u[IL - 1, j] / (h * h)  
# Back side
        w[IL + T, j] = -2 * u[IL + T + 1, j] / (h * h)  
    for i in range(IL, IL + T + 1):
        w[i, H - 1] = -2 * u[i, H] / (h * h)
        # Top
    for i in range(IL, IL + T + 1):
        for j in range(0, H + 1):
# Front
            u[IL, j] = 0.0  
# Back
            u[IL + T, j] = 0.0  
            u[i, H] = 0
            # Top


# Method to relax stream
def relax():  
# Reset conditions at beam
    beam()  
# Relax stream function
    for i in range(1, Nxmax):  
        for j in range(1, Nymax):
            r1 = omega * ( ( u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1] + h * h * w[i, j] ) / 4 - u[i, j] )
            u[i, j] += r1
# Relax vorticity
    for i in range(1, Nxmax):  
        for j in range(1, Nymax):
            a1 = w[i + 1, j] + w[i - 1, j] + w[i, j + 1] + w[i, j - 1]
            a2 = vector(u[i, j + 1] - u[i, j - 1]) * (w[i + 1, j] - w[i - 1, j])
            a3 = vector(u[i + 1, j] - u[i - 1, j]) * (w[i, j + 1] - w[i, j - 1])
            r2 = omega * ((a1 - (R / 4.0) * (a2 - a3)) / 4.0 - w[i, j])
            w[i, j] += r2


m = 0
borders()
while iter <= 300:
    iter += 1
    if iter % 10 == 0:
        print(m)
        m += 1
    relax()
for i in range(0, Nxmax + 1):

    for j in range(0, Nymax + 1):
# stream in V0h units
        u[i, j] = u[i, j] / (V0 * h)  
# u.resize((70,70));
# w.resize((70,70));
# to plot lines in x axis
x = list(range(0, Nxmax - 1))  
y = list(range(0, Nymax - 1))
# x=range(0,69)                   #to plot lines in x axis
# y=range(0,69)
# grid for position and time
X, Y = p.meshgrid(x, y)  


# returns stream flow to plot
def functz(u):  
# for several iterations
    z = u[X, Y]  
    return z


# returns stream flow to plot
def functz1(w):  
# for several iterations
    z1 = w[X, Y]  
    return z1


Z = functz(u)
Z1 = functz1(w)
fig1 = p.figure()
p.title("Stream function - 2D Flow over a beam")
p.imshow(Z, origin="lower")
p.colorbar()
fig2 = p.figure()
p.title("Vorticity - 2D Flow over a beam")
p.imshow(Z1, origin="lower")
p.colorbar()
# Shows the figure, close Python shell to
p.show()  
# Finish watching the figure
print("finished")
