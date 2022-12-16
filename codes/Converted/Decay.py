""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Decay.py spontaneous decay simulation
from visual import *
from visual.graph import *
import random

# Decay constant
lambda1 = 0.01  
max = 50.0
time_max = 500
# Params
seed = 68111  
# Initial value
number = nloop = max  
# random.seed(seed)                               # Seed number generator

graph1 = graph( width=500, height=500, title="Spontaneous Decay", xtitle="Time", ytitle="Number left", xmax=500, xmin=0, ymax=100, ymin=0, )
decayfunc = gcurve(color=color.green)

# Time loop
for time in arange(0, time_max + 1):  
# Decay loop
    for atom in arange(1, number + 1):  
        decay = random.random()
        if decay < lambda1:
# A decay
            nloop = nloop - 1  
    number = nloop
    decayfunc.plot(pos=(time, number))
    rate(30)
