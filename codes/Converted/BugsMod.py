""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# Bugs.py The Logistic map

from visual.graph import *

mu_min = 1.0
mu_max = 4.0
#
step = 0.01  
# To avoid repeat x values
lastx = int(1000 * 0.5)  
# Plot every 2 iterations
count = 0  

graph1 = graph( width=600, height=400, title="Logistic Map", xtitle="mu", ytitle="x*", xmax=4.0, xmin=1.0, ymax=1.0, ymin=0.0, )
pts = gdots(shape="round", size=1.5, color=color.green)

for mu in arange(mu_min, mu_max, step):
# Start ea loop at x=0.5
    x = 0.5  
# Avoid transients
    for i in range(1, 201, 1):  
        x = mu * x * (1 - x)
# Now can plot
    for i in range(201, 402, 1):  
        x = mu * x * (1 - x)
# Truncated x
        intx = int(1000 * x)  
# Avoid repeats
        if intx != lastx and count % 2 == 0:  
# New x & even count
            pts.plot(pos=(mu, x))  
        lastx = intx
        count += 1
