""" From: "A SURVEY OF COMPUTATIONAL PHYSICS" 
   by RH Landau, MJ Paez, and CC BORDEIANU 
   Copyright Princeton University Press, Princeton, 2008.
   Electronic Materials copyright: R Landau, Oregon State Univ, 2008;
   MJ Paez, Univ Antioquia, 2008; and CC BORDEIANU, Univ Bucharest, 2008.
   Support by National Science Foundation """

# Simulates radiactive decay
from visual import *
from visual.graph import *
# generates random numbers
import random  

# grid 100x100
rejilla = ones((100, 100))  
escena = canvas( x=0, y=0, width=400, height=400, range=120, title="Simulates radiactive decay"
# to see atoms
)  
# to see decay cruve
graph = graph( x=0, y=400, width=600, height=400, title="Nuclei left", xtitle="time (s)", ytitle="N(t)", xmax=50000, xmin=0.0, ymax=2000, ymin=0, foreground=color.black, background=color.white, )  
# curve in red, instance of gcurve
restantes = gcurve(color=color.red)  
# At beginning  0 atoms
Natomos = 0  


# put atoms at random in grid
def atomos():  
# to know the number
    global Natomos  
    for i in range(0, 2000):
# coord. x integer 0<=x<=100
        x = int(100 * random.random())  
# coord. y integer 0<=y<=100
        y = int(100 * random.random())  
# empty this position?
        if rejilla[x][y] == 1:  
# x screen position
            xpos = 2 * x - 100  
# y screen position
            ypos = 2 * y - 100  
# atom
            sphere(pos=vector(xpos, ypos,0), color=color.green, radius=2.0)  
# occupied cell
            rejilla[x][y] = 0  
# another atom placed
            Natomos += 1  
# numero de atomos colocados
    print(Natomos)  


# calcula y grafica el decaimiento
def decaimiento():  
# use el valor que calculo de Natomos
    global Natomos  
# la llama para colocar los atomos
    atomos()  
# constante de decaimiento
    constdec = 0.8  
    print(Natomos)

# 50000 events
    for t in range(0, 50000):  
# slow action
        rate(3000)  
# generates coord. x  0 to 100
        x = int(100 * random.random())  
# generates y coord. between 0 - 100
        y = int(100 * random.random())  
# random number between 0 and 1
        r = random.random()  
        # following: if atom at xy, if r< decay constant
        # and if atoms to decay
        if rejilla[x][y] == 0 and r < constdec and Natomos > 0:
# atom decay
            Natomos -= 1  
# coord x in screen
            xpos = 2 * x - 100  
# coord y in screen
            ypos = 2 * y - 100  
            sphere(pos=vector(xpos, ypos,0), color=color.white, radius=2.0)
# indicates atom at that point decayed
            rejilla[x][y] = 2  
# plot nondecayed atoms
            restantes.plot(pos=(t, Natomos))  


decaimiento()
