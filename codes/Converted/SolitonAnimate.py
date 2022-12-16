""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# SolitonAnimate.py: Solves KdeV equation for a soliton

from vpython import *

# Set up plot
g = canvas(width=600, height=300, title="Soliton")
sol = curve(x=list(range(0, 131)), color=color.yellow)

# Parameters
# thickness of line
sol.radius = 1.0  
# Delta x
ds = 0.4  
# Delta t
dt = 0.1  
# Numb t steps
max = 2000  
mu = 0.1
# Mu from KdeV equation
eps = 0.2
# Epsilon from KdeV eq
# grid in x max
mx = 131  
# combor
fac = mu * dt / (ds**3)  

# Initialization
# Soliton amplitude
u = zeros((mx, 3), float)  

# Initial wave
for i in range(0, 131):  
    u[i, 0] = 0.5 * ( 1.0 - ( (math.exp(2 * (0.2 * ds * i - 5.0)) - 1) / (math.exp(2 * (0.2 * ds * i - 5.0)) + 1) ) )
u[0, 1] = 1.0
u[0, 2] = 1.0
u[130, 1] = 0.0
# End points
u[130, 2] = 0.0  

for i in range(0, 131):
    sol.x[i] = 2 * i - 130.0
    sol.y[i] = 50.0 * u[i, 0] - 30

# First time step
for i in range(1, mx - 1):  
    a1 = eps * dt * (u[i + 1, 0] + u[i, 0] + u[i - 1, 0]) / (ds * 6.0)
    if i > 1 and i < 129:
        a2 = u[i + 2, 0] + 2.0 * u[i - 1, 0] - 2.0 * u[i + 1, 0] - u[i - 2, 0]
    else:
        a2 = u[i - 1, 0] - u[i + 1, 0]
    a3 = u[i + 1, 0] - u[i - 1, 0]
    u[i, 1] = u[i, 0] - a1 * a3 - fac * a2 / 3.0

for i in range(0, 131):
    sol.x[i] = 2 * i - 130.0
    sol.y[i] = 50.0 * u[i, 1] - 30

for j in range(1, max + 1):
# Following next time steps
    rate(150)  
    for i in range(1, mx - 2):
        a1 = eps * dt * (u[i + 1, 1] + u[i, 1] + u[i - 1, 1]) / (3.0 * ds)
        if i > 1 and i < mx - 2:
            a2 = u[i + 2, 1] + 2 * u[i - 1, 1] - 2 * u[i + 1, 1] - u[i - 2, 1]
        else:
            a2 = u[i - 1, 1] - u[i + 1, 1]
        a3 = u[i + 1, 1] - u[i - 1, 1]
        u[i, 2] = u[i, 0] - a1 * a3 - 2.0 * fac * a2 / 3.0
# Plot every 100 time steps
    if j % 5 == 0:  
        for i in range(0, mx - 2):
            sol.x[i] = 2 * i - 130
            sol.y[i] = 50.0 * u[i, 2] - 30
        sol.pos
# Recycle array
    for k in range(0, mx):  
        u[k, 0] = u[k, 1]
        u[k, 1] = u[k, 2]
        # Finish plot
print("finished")
