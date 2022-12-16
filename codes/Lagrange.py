"""Dirichlet boundary conditions surrounding four walls 
 Domain dimensions: WxH, with 2 triangles per square  
 Based on FEM2DL_Box Matlab program in Polycarpou, Intro to the Finite 
 Element Method in Electromagnetics, Morgan & Claypool (2006) """


# Lagrange.py: Langrange interpolation tabulated data; 2, 4, 8 degree poly

from vpython import *
from vpython import *
from vpython import *

sceneK = canvas( x=0, y=0, width=500, height=500, title="Lagrange Interpolation with Toggle Switch"
)
graph = curve(color=color.yellow, x=list(range(0, 201)), radius=3)
xin = array([0, 25, 50, 75, 100, 125, 150, 175, 200])
yin = array([10.6, 6, 45, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])
# Poits to fit
expts = []  
yy = zeros((204), float)
w = 150
c = controls(x=300, y=50, width=w, height=w, range=60)
t1 = toggle( pos=vector(0, 0,0), width=30, height=30, text0="1 polynom deg 8", text1="4 polynms deg. 2", action=lambda: selectpoly(), )


def selectpoly():
# Change previous value
    global polinom  
    if t1.value:
        polinom = 3
    else:
        polinom = 9


def axis():
    xmin = -200
    xmax = 200
    xincr = 100
    yincr = 400.0 / 6.0
    ymin = -200
    ymax = 200
    curve(color=color.white, pos=[(-200, -200), (200, -200)])
    curve(color=color.white, pos=[(-200, -200), (-200, 200)])
# x tics & labels
    for i in range(0, 5):  
        curve( pos=[(xmin + xincr * i, ymin), (xmin + xincr * i, ymin - 10)], color=color.white, )
        xnum = i * 50
        xtext = str(xnum)
        label(pos=vector(xmin + xincr * i, ymin - 30,0), color=color.white, box=0, text=xtext)
# y tics & labels
    for i in range(0, 7):  
        ynum = i * 15
        ytext = str(ynum)
        curve( pos=[(xmin - 10, ymin + yincr * i), (xmin, ymin + yincr * i)], color=color.white, )
        label(pos=vector(xmin - 30, ymin + yincr * i,0), color=color.white, box=0, text=ytext)


# Data
def points():  
    for i in range(0, 9):
# x linear trsn. from 0->100 to -200->200
        xc = 2 * xin[i] - 200  
# y linear trsn. from 0->90  to -200->200
        yc = 40 * yin[i] / 9.0 - 200  
        expts.append(sphere(pos=vector(xc, yc,0), radius=8, color=color.red))


# poly interpolation beg:begining
def legendrepol(x, beg, finish):  
    y = 0.0
    for i in range(beg, finish + 1):
        lambd = 1.0
        for j in range(beg, finish + 1):
# Lagrange polynom formed here
            if i != j:  
                lambd *= (x - xin[j - 1]) / (xin[i - 1] - xin[j - 1])
        y += yin[i - 1] * lambd
    return y


def plotpoly():
    axis()
# 8th degree poly
    points()  
    if polinom == 9:
        xx = 0.0
        for k in range(0, 201):
            yy[k] = legendrepol(xx, 1, 9)
            xc = 2 * xx - 200
            yc = 40 * yy[k] / 9.0 - 200
            graph.x[k] = xc
            graph.y[k] = yc
            xx += 1.0
    graph.pos
# 2nd degree poly's
    if polinom == 3:  
        xx = 0.0
        startat = 0
        for mm in range(1, 8, 2):
            for k in range(startat, startat + 50 + 1):
                xx = 1.0 * k
                yy[k] = legendrepol(xx, mm, mm + 2)
                xc = 2 * xx - 200
                yc = 40 * yy[k] / 9.0 - 200
                graph.x[k] = xc
                graph.y[k] = yc
            graph.pos
            startat = startat + 50


polinom = 9
while 1:
# Checks toggle switch
    c.interact()  
    plotpoly()
