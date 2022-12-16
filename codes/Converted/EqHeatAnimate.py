""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# EqHeat.py Animated heat equation soltn via fine differences

from vpython import *
from vpython import *

g = canvas(width=600, height=300, title="Cooling of Bar, T(t=0) = 100, T(x=0,L)=0")
# Temperature Curve, its parameters and labels
tempe = curve(x=list(range(0, 101)), color=color.red)
tempe.radius = 1.0
yax = curve(pos=[(0, -20), (0, 40)], color=color.yellow)
maxT = label(text="100", pos=vector(0, 50,0), box=0)
minT = label(text="0", pos=vector(0, -25,0), box=0)
bar = curve(pos=[(-100, -20), (100, -20)], color=color.magenta)
thisbar = label(text="Bar", pos=vector(15, -20,0), xoffset=15, yoffset=-15)
ball1 = sphere(pos=vector(100, -20,0), color=color.blue, radius=4)
ball2 = sphere(pos=vector(-100, -20,0), color=color.blue, radius=4)

# Parameters
# Grid points in x
Nx = 101  
# x increment
Dx = 0.01414  
# t increment
Dt = 1.0  
# Thermal conductivity
KAPPA = 210.0  
# Specific heat
SPH = 900.0  
# Density
RHO = 2700.0  
# Temp @ first 2 times
T = zeros((Nx, 2), float)  

# Initial temperature in the bar
for ix in range(1, Nx - 1):  
    T[ix, 0] = 100.0


# Ends of bar at T = 0
T[0, 0] = 0.0  
T[0, 1] = 0.0
T[Nx - 1, 0] = 0.0
T[Nx - 1, 1] = 0.0
# Constant combo in algorthim
cons = KAPPA / (SPH * RHO) * Dt / (Dx * Dx)  

for i in range(0, Nx - 1):
# Scaled x's
    tempe.x[i] = 2.0 * i - 100.0  
# Scaled y's (Temp)
    tempe.y[i] = 0.8 * T[i, 0] - 20.0  

while 1:
    rate(150)
    for ix in range(1, Nx - 1):
        T[ix, 1] = T[ix, 0] + cons * (T[ix + 1, 0] + T[ix - 1, 0] - 2.0 * T[ix, 0])
    for i in range(0, Nx):
# Scale 0<x<100 -> -100<x<100
        tempe.x[i] = 2.0 * i - 100.0  
        tempe.y[i] = 0.6 * T[i, 1] - 20.0

    for ix in range(1, Nx - 1):
# Row of 100 positions at t = m
        T[ix, 0] = T[ix, 1]  
