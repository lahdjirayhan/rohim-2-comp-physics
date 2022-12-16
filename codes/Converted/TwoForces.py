""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# TwoForces.py Forces on two moving strings

from visual.graph import *

posy = 100
# basic height, cord length
Lcord = 250  
Hweight = 50
# cylinder height, weight
W = 10  

scene = canvas(heigth=600, width=600, range=380)
alt = curve(pos=[(-300, posy, 0), (300, posy, 0)])
divi = curve(pos=[(0, -150, 0), (0, posy, 0)])
# kg as a cylinder
kilogr = cylinder( pos=vector(0, posy - Lcord, 0), radius=20, axis=vector(0, -Hweight, 0), color=color.red )  
cord1 = cylinder(pos=vector(0, posy, 0), axis=vector(0, -Lcord, 0), color=color.yellow, radius=2)
cord2 = cylinder(pos=vector(0, posy, 0), axis=vector(0, -Lcord, 0), color=color.yellow, radius=2)

# Tension cord 1
arrow1 = arrow(pos=vector(0, posy, 0), color=color.orange)  
# Tension cord 2
arrow2 = arrow(pos=vector(0, posy, 0), color=color.orange)  

# initial force of each student
magF = W / 2.0  
# (m/s) velocity of each student
v = 2.0  
# initial position student 1
x1 = 0.0  
anglabel = label(pos=vector(0, 240, 0), text="angle (deg)", box=0)
angultext = label(pos=vector(20, 210, 0), box=0)
Flabel1 = label(pos=vector(200, 240, 0), text="Force", box=0)
Ftext1 = label(pos=vector(200, 210, 0), box=0)
Flabel2 = label(pos=vector(-200, 240, 0), text="Force", box=0)
Ftext2 = label(pos=vector(-200, 210, 0), box=0)
# light
local_light(pos=vector(-10, 0, 20), color=color.yellow)  

for t in arange(0.0, 100.0, 0.2):
# slow motion
    rate(50)  
# 1 to right, 2 to left
    x1 = v * t  
# angle cord
    theta = asin(x1 / Lcord)  
# cylinder height
    poscil = posy - Lcord * cos(theta)  
# y-position kilogram
    kilogr.pos = vector(0, poscil, 0)  
# Cord tension
    magF = W / (2.0 * cos(theta))  
    angle = 180.0 * theta / pi
# position cord end
    cord1.pos = vector(x1, posy, 0)  
    cord1.axis = vector(-Lcord * sin(theta), -Lcord * cos(theta), 0)
# position end cord
    cord2.pos = vector(-x1, posy, 0)  
    cord2.axis = vector(Lcord * sin(theta), -Lcord * cos(theta), 0)
# axis arrow
    arrow1.pos = cord1.pos  
    arrow1.axis = vector(8 * magF * sin(theta), 8 * magF * cos(theta), 0)
    arrow2.pos = cord2.pos
    arrow2.axis = vector(-8 * magF * sin(theta), 8 * magF * cos(theta), 0)
    angultext.text = "%4.2f" % angle
    force = magF
# Tension
    Ftext1.text = "%8.2f" % force  
    Ftext2.text = "%8.2f" % force
