""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# BurgerLax.py:   Solve Burger's eqnt via Lax-Wendroff scheme
# du/dt+ c*d(u**2/2)/dx=0;   u(x,t=0)=exp(-300(x-0.12)**2)

from visual.graph import *

# No steps in x
m = 100  
c = 1.0
dx = 1.0 / m
# beta = c*dt/dx
beta = 0.8  
u = [0] * (m + 1)
# Initial Numeric
u0 = [0] * (m + 1)
uf = [0] * (m + 1)
dt = beta * dx / c
T_final = 0.5
# N time steps
n = int(T_final / dt)  

graph1 = graph( width=600, height=500, xtitle="x", xmin=0, xmax=1, ymin=0, ymax=1, ytitle="u(x), Cyan=exact, Yellow=Numerical", title="Advection Eqn: Initial (red), Exact (cyan),\
         Numerical Lax-Wendroff (yellow)",
)
initfn = gcurve(color=color.red)
exactfn = gcurve(color=color.cyan)
# Numerical solution
numfn = gcurve(color=color.yellow)  


# Plot initial & exact solution
def plotIniExac():  
    for i in range(0, m):
        x = i * dx
# Gaussian initial
        u0[i] = exp(-300.0 * (x - 0.12) ** 2)  
# Initial function
        initfn.plot(pos=(0.01 * i, u0[i]))  
# Exact in cyan
        uf[i] = exp(-300.0 * (x - 0.12 - c * T_final) ** 2)  
        exactfn.plot(pos=(0.01 * i, uf[i]))
        rate(50)


plotIniExac()


# Finds Lax Wendroff solution
def numerical():  
#  Time loop
    for j in range(0, n + 1):  
#   x loop
        for i in range(0, m - 1):  
# Algorithm
            u[i + 1] = ( (1.0 - beta * beta) * u0[i + 1] - (0.5 * beta) * (1.0 - beta) * u0[i + 2] + (0.5 * beta) * (1.0 + beta) * u0[i] )  
            u[0] = 0.0
            u[m - 1] = 0.0
            u0[i] = u[i]


numerical()
for j in range(0, m - 1):
    rate(50)
# Plot numerical Solution
    numfn.plot(pos=(0.01 * j, u[j]))  
