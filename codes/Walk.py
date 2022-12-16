""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Walk.py  Random walk with graph
from vpython import *
from vpython import *
import random

# None => system clock
random.seed(None)  
jmax = 20
x = 0.0
# Start at origin
y = 0.0  

graph1 = graph(width=500, height=500, title="Random Walk", xtitle="x", ytitle="y")
pts = gcurve(color=color.yellow)

for i in range(0, jmax + 1):
# Plot points
    pts.plot(pos=(x, y))  
# -1 =< x =< 1
    x += (random.random() - 0.5) * 2.0  
# -1 =< y =< 1
    y += (random.random() - 0.5) * 2.0  
    pts.plot(pos=(x, y))
    rate(100)
