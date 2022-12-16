""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# QMC.py: Quantum MonteCarlo (Feynman path integration)

from vpython import *
from vpython import *
import random

N = 100
Nsteps = 101
# Initialize
xscale = 10.0  
path = zeros([Nsteps], float)
prob = zeros([Nsteps], float)

trajec = canvas(width=300, height=500, title="Spacetime Paths")
trplot = curve(y=list(range(0, 100)), color=color.magenta, canvas=trajec)


# Axis
def PlotAxes():  
    trax = curve(pos=[(-97, -100), (100, -100)], colo=color.cyan, canvas=trajec)
    label(pos=vector(0, -110,0), text="0", box=0, canvas=trajec)
    label(pos=vector(60, -110,0), text="x", box=0, canvas=trajec)


# Axes for probability
def WaveFunctionAxes():  
    wvfax = curve(pos=[(-600, -155), (800, -155)], canvas=wvgraph, color=color.cyan)
    curve(pos=[(0, -150), (0, 400)], canvas=wvgraph, color=color.cyan)
    label(pos=vector(-80, 450,0), text="Probability", box=0, canvas=wvgraph)
    label(pos=vector(600, -220,0), text="x", box=0, canvas=wvgraph)
    label(pos=vector(0, -220,0), text="0", box=0, canvas=wvgraph)


# HO Energy
def Energy(path):  
    sums = 0.0
    for i in range(0, N - 2):
        sums += (path[i + 1] - path[i]) * (path[i + 1] - path[i])
    sums += path[i + 1] * path[i + 1]
    return sums


# Plot trajectory
def PlotPath(path):  
    for j in range(0, N):
        trplot.x[j] = 20 * path[j]
        trplot.y[j] = 2 * j - 100


# Plot prob
def PlotWF(prob):  
    for i in range(0, 100):
        wvplot.color = color.yellow
# Center fig
        wvplot.x[i] = 8 * i - 400  


wvgraph = canvas(x=340, y=150, width=500, height=300, title="Ground State")
wvplot = curve(x=list(range(0, 100)), canvas=wvgraph)
wvfax = curve(color=color.cyan)
PlotAxes()
# Plot axes
WaveFunctionAxes()  
oldE = Energy(path)
# Pick random element
while True:  
# Slow paintings
    rate(10)  
# Metropolis
    element = int(N * random.random())  
    change = 2.0 * (random.random() - 0.5)
# Change path
    path[element] += change  
    newE = Energy(path)
    # Find new E
    if newE > oldE and math.exp(-newE + oldE) <= random.random():
# Reject
        path[element] -= change  
# Plot trajectory
        PlotPath(path)  
# if path = 0, elem = 50
    elem = int(path[element] * 16 + 50)  

    # elem = m *path[element] + b is the linear transformation
    # if path=-3, elem=2 if path=3., elem=98 => b=50, m=16 linear TF
    # this way x = 0 correspond to prob[50]

    if elem < 0:
        elem = vector(0,,0)
    if elem > 100:
# If exceed max
        elem = 100  
# increase probability
    prob[elem] += 1  
# Plot prob
    PlotWF(prob)  
    oldE = newE
