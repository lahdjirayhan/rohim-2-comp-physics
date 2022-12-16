""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# DecaySound.py spontaneous decay simulation

from vpython import *
from vpython import *
import random, winsound

# Decay constant
lambda1 = 0.005  
max = 80.0
time_max = 500
seed = 68111
# Initial value
number = nloop = max  
graph1 = graph(title="Spontaneous Decay", xtitle="Time", ytitle="Number")
decayfunc = gcurve(color=color.green)

# Time loop
for time in arange(0, time_max + 1):  
# Decay loop
    for atom in arange(1, number + 1):  
        decay = random.random()
        if decay < lambda1:
# A decay
            nloop = nloop - 1  
# Sound beep
            winsound.Beep(600, 100)  
    number = nloop
    decayfunc.plot(pos=(time, number))
    rate(30)
