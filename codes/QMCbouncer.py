""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# QMCbouncer.py:       g.s. wavefunction via path integration

from vpython import *
import random
from vpython import *

# Parameters
N = 100
dt = 0.05
g = 2.0
h = 0.00
maxel = 0
path = zeros([101], float)
arr = path
prob = zeros([201], float)

trajec = canvas(width=300, height=500, title="Spacetime Trajectory")
trplot = curve(y=list(range(0, 100)), color=color.magenta, canvas=trajec)


# plot axis for trajectories
def trjaxs():  
    trax = curve(pos=[(-97, -100), (100, -100)], color=color.cyan, canvas=trajec)
    curve(pos=[(-65, -100), (-65, 100)], color=color.cyan, canvas=trajec)
    label(pos=vector(-65, 110,0), text="t", box=0, canvas=trajec)
    label(pos=vector(-85, -110,0), text="0", box=0, canvas=trajec)
    label(pos=vector(60, -110,0), text="x", box=0, canvas=trajec)


wvgraph = canvas(x=350, y=80, width=500, height=300, title="GS Prob")
# wave function plot
wvplot = curve(x=list(range(0, 50)), canvas=wvgraph)  
wvfax = curve(color=color.cyan)


# plot axis for wavefunction
def wvfaxs():  
    wvfax = curve(pos=[(-200, -155), (800, -155)], canvas=wvgraph, color=color.cyan)
    curve(pos=[(-200, -150), (-200, 400)], canvas=wvgraph, color=color.cyan)
    label(pos=vector(-70, 420,0), text="Probability", box=0, canvas=wvgraph)
    label(pos=vector(600, -220,0), text="x", box=0, canvas=wvgraph)
    label(pos=vector(-200, -220,0), text="0", box=0, canvas=wvgraph)


trjaxs()
# plot axes
wvfaxs()  


# Energy of path
def energy(arr):  
    esum = 0.0
    for i in range(0, N):
        esum += 0.5 * ((arr[i + 1] - arr[i]) / dt) ** 2 + g * (arr[i] + arr[i + 1]) / 2
    return esum


# Plot xy trajectory
def plotpath(path):  
    for j in range(0, N):
        trplot.x[j] = 20 * path[j] - 65
        trplot.y[j] = 2 * j - 100


# Plot wave function
def plotwvf(prob):  
    for i in range(0, 50):
        wvplot.color = color.yellow
        wvplot.x[i] = 20 * i - 200
        wvplot.y[i] = 0.5 * prob[i] - 150


oldE = energy(path)
counter = 1
# plot psi every 100
norm = 0.0  
maxx = 0.0

# "Infinite" loop
while 1:  
    rate(100)
    element = int(N * random.random())
# Ends not allowed
    if element != 0 and element != N:  
        change = ((random.random() - 0.5) * 20.0) / 10.0
# No negative paths
        if path[element] + change > 0.0:  
            path[element] += change
# New trajectory E
            newE = energy(path)  
            if newE > oldE and exp(-newE + oldE) <= random.random():
# Link rejected
                path[element] -= change  
                plotpath(path)
# Scale changed
            ele = int(path[element] * 1250.0 / 100.0)  
            if ele >= maxel:
# Scale change 0 to N
                maxel = ele  
            if element != 0:
                prob[ele] += 1
            oldE = newE
# plot psi every 100
    if counter % 100 == 0:  
# max x of path
        for i in range(0, N):  
            if path[i] >= maxx:
                maxx = path[i]
# space step
        h = maxx / maxel  
# for trap. extremes
        firstlast = h * 0.5 * (prob[0] + prob[maxel])  
        for i in range(0, maxel + 1):
# norm
            norm = norm + prob[i]  
# Trap rule
        norm = norm * h + firstlast  
# plot probability
        plotwvf(prob)  
    counter += 1
