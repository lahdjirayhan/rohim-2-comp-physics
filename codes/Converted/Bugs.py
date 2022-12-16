""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Bugs.py The Logistic map

from visual.graph import *

m_min = 1.0
m_max = 4.0
step = 0.01
graph1 = graph( width=600, height=400, title="Logistic Map", xtitle="m", ytitle="x", xmax=4.0, xmin=1.0, ymax=1.0, ymin=0.0, )
pts = gdots(shape="round", size=1.5, color=color.green)
# Eliminates some points
lasty = int(1000 * 0.5)  
# Plot every 2 iterations
count = 0  
for m in arange(m_min, m_max, step):
    y = 0.5
# Avoid transients
    for i in range(1, 201, 1):  
        y = m * y * (1 - y)
    for i in range(201, 402, 1):
        y = m * y * (1 - y)
# Avoid transients
    for i in range(201, 402, 1):  
        oldy = int(1000 * y)
        y = m * y * (1 - y)
        inty = int(1000 * y)
        if inty != lasty and count % 2 == 0:
# Avoid repeats
            pts.plot(pos=(m, y))  
        lasty = inty
        count += 1
