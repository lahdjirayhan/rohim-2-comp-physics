""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Walk3D.py  3-D Random walk with 3-D graph

from visual import *
import random

# None => system clock
random.seed(None)  
jmax = 1000
# Start at origin
xx = yy = zz = 0.0  

graph1 = canvas( x=0, y=0, width=600, height=600, title="3D Random Walk", forward=vector(-0.6, -0.5, -1) )
pts = curve(x=list(range(0, 100)), radius=10.0, color=color.yellow)
xax = curve( x=list(range(0, 1500)), color=color.red, pos=[(0, 0, 0), (1500, 0, 0)], radius=10.0 )
yax = curve( x=list(range(0, 1500)), color=color.red, pos=[(0, 0, 0), (0, 1500, 0)], radius=10.0 )
zax = curve( x=list(range(0, 1500)), color=color.red, pos=[(0, 0, 0), (0, 0, 1500)], radius=10.0 )
xname = label(text="X", pos=vector(1000, 150, 0), box=0)
yname = label(text="Y", pos=vector(-100, 1000, 0), box=0)
zname = label(text="Z", pos=vector(100, 0, 1000), box=0)

# Starting point
pts.x[0] = pts.y[0] = pts.z[0] = 0  
for i in range(1, 100):
# -1 =< x =< 1
    xx += (random.random() - 0.5) * 2.0  
# -1 =< y =< 1
    yy += (random.random() - 0.5) * 2.0  
# -1 =< z =< 1
    zz += (random.random() - 0.5) * 2.0  
    pts.x[i] = 200 * xx - 100
    pts.y[i] = 200 * yy - 100
    pts.z[i] = 200 * zz - 100
    rate(100)
print(("Walk's distance R =", sqrt(xx * xx + yy * yy + zz * zz)))
