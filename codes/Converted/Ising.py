""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2011; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2011.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# Ising.py: Ising model
from visual import *
import random
from visual.graph import *

# Display for the arrows
scene = canvas(x=0, y=0, width=700, height=200, range=40, title="Spins")
engraph = graph( y=200, width=700, height=300, title="E of Spin System", xtitle="iteration", ytitle="E", xmax=500, xmin=0, ymax=5, ymin=-5, )
# for the energy plot
enplot = gcurve(color=color.yellow)  
# number of spins
N = 30  
# magnetic field
B = 1.0  
# g mu (giromag. times Bohrs magneton)
mu = 0.33  
# Exchange energy
J = 0.20  
# Boltmann constant
k = 1.0  
# Temperature
T = 100.0  
# spins state some up(1) some down (0)
state = zeros((N))  
S = zeros((N), float)
# a test state
test = state  
# Seed random generator
random.seed()  


# Method to calc energy
def energy(S):  
    FirstTerm = 0.0
# Sum  energy
    SecondTerm = 0.0  
    for i in range(0, N - 2):
        FirstTerm += S[i] * S[i + 1]
    FirstTerm *= -J
    for i in range(0, N - 1):
        SecondTerm += S[i]
    SecondTerm *= -B * mu
    return FirstTerm + SecondTerm


# State, test's energy
ES = energy(state)  


# Plots spins according to state
def spstate(state):  
    for obj in scene.objects:
#  erase previous arrows
        obj.visible = 0  
    j = 0
# 30 spins numbered from 0 to 29
    for i in range(-N, N, 2):  
        if state[j] == -1:
# case spin down
            ypos = 5  
        else:
            ypos = 0
        if 5 * state[j] < 0:
# white arrow if spin down
            arrowcol = vector(1, 1, 1)  
        else:
            arrowcol = vector(0.7, 0.8, 0)
# arrow
        arrow(pos=vector(i, ypos, 0), axis=vector(0, 5 * state[j], 0), color=arrowcol)  
        j += 1


for i in range(0, N):
# initial state, all spins down
    state[i] = -1  

for obj in scene.objects:
    obj.visible = 0
# plots initial state: all spins down
spstate(state)  
# finds the energy of the spin system
ES = energy(state)  
# Here is the Metropolis algorithm
# Change state and test
for j in range(1, 500):  
# to be able to see the flipping
    rate(3)  
# test is the previous spin state
    test = state  
    r = int(N * random.random())
    # Flip spin randomly
# flips temporarily that spin
    test[r] *= -1  
# finds energy of the test configur.
    ET = energy(test)  
# test with Boltzmann factor
    p = math.exp((ES - ET) / (k * T))  
# adds a segment to the curve of E
    enplot.plot(pos=(j, ES))  
# to see if trial config. is accepted
    if p >= random.random():  
        state = test
        spstate(state)
        ES = ET
