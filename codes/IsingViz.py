""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# IsingViz.py: Ising model

"""Dirichlet boundary conditions surrounding four walls 
 Domain dimensions: WxH, with 2 triangles per square  
 Based on FEM2DL_Box Matlab program in Polycarpou, Intro Finite 
 Element Method in Electromagnetics, Morgan & Claypool (2006) """

from vpython import *
import random
from vpython import *

# Display for the arrows
scene = canvas(x=0, y=0, width=700, height=200, range=40, title="Spins")
engraph = graph( y=200, width=700, height=300, title="E of Spin System", xtitle="iteration", ytitle="E", xmax=500, xmin=0, ymax=5, ymin=-5, )
enplot = gcurve(color=color.yellow)
N = 30
B = 1.0
# g mu
mu = 0.33  
J = 0.20
# Boltmann
k = 1.0  
T = 100.0
# spins up(1), down (0)
state = zeros((N))  
S = zeros((N), float)
test = state
# Seed generator
random.seed()  


def energy(S):
    FirstTerm = 0.0
    SecondTerm = 0.0
    for i in range(0, N - 2):
        FirstTerm += S[i] * S[i + 1]
    FirstTerm *= -J
    for i in range(0, N - 1):
        SecondTerm += S[i]
    SecondTerm *= -B * mu
    return FirstTerm + SecondTerm


ES = energy(state)


# Plots spins
def spstate(state):  
    for obj in scene.objects:
# Erase arrows
        obj.visible = 0  
    j = 0
    for i in range(-N, N, 2):
        if state[j] == -1:
# Spin down
            ypos = 5  
        else:
            ypos = 0
        if 5 * state[j] < 0:
# White = down
            arrowcol = vector(1, 1, 1)  
        else:
            arrowcol = vector(0.7, 0.8, 0)
        arrow(pos=vector(i, ypos, 0), axis=vector(0, 5 * state[j], 0), color=arrowcol)
        j += 1


for i in range(0, N):
# Initial spins all down
    state[i] = -1  

for obj in scene.objects:
    obj.visible = 0
spstate(state)
ES = energy(state)

for j in range(1, 500):
    rate(3)
    test = state
    r = int(N * random.random())
    # Flip spin randomly
    test[r] *= -1
    ET = energy(test)
#  Boltzmann test
    p = math.exp((ES - ET) / (k * T))  
# Adds segment to curve
    enplot.plot(pos=(j, ES))  
    if p >= random.random():
        state = test
        spstate(state)
        ES = ET
