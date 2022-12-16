""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

#  vonNeuman: Monte-Carlo integration via stone throwing

import random
from visual.graph import *

# points to plot the function
N = 100  
graph = canvas(width=500, height=500, title="vonNeumann Rejection Int")
xsinx = curve(x=list(range(0, N)), color=color.yellow, radius=0.5)
# Labels
pts = label(pos=vector(-60, -60,0), text="points=", box=0)  
pts2 = label(pos=vector(-30, -60,0), box=0)
inside = label(pos=vector(30, -60,0), text="accepted=", box=0)
inside2 = label(pos=vector(60, -60,0), box=0)
arealbl = label(pos=vector(-65, 60,0), text="area=", box=0)
arealbl2 = label(pos=vector(-35, 60,0), box=0)
areanal = label(pos=vector(30, 60,0), text="analytical=", box=0)
zero = label(pos=vector(-85, -48,0), text="0", box=0)
five = label(pos=vector(-85, 50,0), text="5", box=0)
twopi = label(pos=vector(90, -48,0), text="2pi", box=0)


def fx(x):
# Integrand
    return x * sin(x) * sin(x)  


# Plot function
def plotfunc():  
    incr = 2.0 * pi / N
    for i in range(0, N):
        xx = i * incr
        xsinx.x[i] = (80.0 / pi) * xx - 80
        xsinx.y[i] = 20 * fx(xx) - 50
# box
    box = curve( pos=[(-80, -50), (-80, 50), (80, 50), (80, -50), (-80, -50)], color=color.white )  


# Box area = h x w =5*2pi
plotfunc()  
j = 0
# Pts inside box
Npts = 3001  
# Analytical integral
analyt = (pi) ** 2  
areanal.text = "analytical=%8.5f" % analyt
genpts = points(size=2)
# points inside box
for i in range(1, Npts):  
#  slow process
    rate(500)  
    x = 2.0 * pi * random.random()
    y = 5 * random.random()
    xp = x * 80.0 / pi - 80
    yp = 20.0 * y - 50
    pts2.text = "%4s" % i
# Below curve
    if y <= fx(x):  
        j += 1
        genpts.append(pos=vector(xp, yp,0), color=color.cyan)
        inside2.text = "%4s" % j
    else:
        genpts.append(pos=vector(xp, yp,0), color=color.green)
    boxarea = 2.0 * pi * 5.0
    area = boxarea * j / (Npts - 1)
    arealbl2.text = "%8.5f" % area
