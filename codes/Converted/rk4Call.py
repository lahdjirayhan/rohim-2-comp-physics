""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# rk4Call.py: 4th O Runge Kutta calling rk4Algor
#           for ODE y" = -100y-2y'+ 100 sin(3t)

from visual.graph import *
from rk4Algor import rk4Algor


Tstart = 0.0
Tend = 10.0
#  Initialization
Nsteps = 100  
y = zeros((2), float)
graph1 = graph( x=0, y=0, width=400, height=400, title="RK4", xtitle="t", ytitle="y[0] = Position versus Time", xmin=0, xmax=10, ymin=-2, ymax=3, )
funct1 = gcurve(color=color.yellow)
graph2 = graph( x=400, y=0, width=400, height=400, title="RK4", xtitle="t", ytitle="y[1] = Velocity versus Time", xmin=0, xmax=10, ymin=-25, ymax=18, )
funct2 = gcurve(color=color.red)
y[0] = 3.0
# Initial position & velocity
y[1] = -5.0  
t = Tstart
h = (Tend - Tstart) / Nsteps


# Force (RHS) function
def f(t, y):  
    fvector = zeros((2), float)
    fvector[0] = y[1]
    fvector[1] = -100.0 * y[0] - 2.0 * y[1] + 10.0 * sin(3.0 * t)
    return fvector


# Time loop
while t < Tend:  
    if (t + h) > Tend:
# Last step
        h = Tend - t  
    y = rk4Algor(t, h, 2, y, f)
    t = t + h
    rate(30)
    funct1.plot(pos=(t, y[0]))
    funct2.plot(pos=(t, y[1]))
