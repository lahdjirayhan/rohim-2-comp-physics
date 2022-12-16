from vpython import *

# initialize wave function, probability, potential
dx = 0.04
dx2 = dx * dx
k0 = 1.0
dt = dx2 / 18.0
xmax = 6.0
# array of x positions
xs = arange(-xmax, xmax, dx)  
# 300= 2*xmax/dx
nmax = 300  
g = canvas( width=500, height=500, title="Wave packet in two wells", background=color.white, foreground=color.black, )
# to plot packet
PlotObj = curve(x=xs, color=color.red, radius=0.02)  
# to plot potential
potential = curve(x=xs, color=color.black, radius=0.02)  
# potential
v = zeros((nmax), float)  
# for real part wave function
psr = zeros((nmax + 1), float)  
# for imaginary part wave function
psi = zeros((nmax + 1), float)  
# counter
i = 0  
for x in arange(-xmax, 0, dx):
    i = i + 1
# left hand side potential
    v[i] = 20 * (x + 2.5) ** 2  
# start right hand side potential
i = 149  
# right hand side potential
for x in arange(0, xmax, dx):  
    v[i] = 20 * (x - 2.5) ** 2
    i = i + 1
# initial condition; wave packet
prob = zeros((nmax + 1), float)  
# Re wave function Psi
psr = exp(-5.5 * ((xs + 4.5)) ** 2) * cos(k0 * xs)  
# Im wave function Psi
psi = exp(-5.5 * ((xs + 4.5)) ** 2) * sin(k0 * xs)  
# probability =wavefunction**2
prob = psr * psr + psi * psi  
j = 0
for x in arange(-xmax, xmax, dx):
# x component
    PlotObj.x[j] = x  
# 5* probability lowered 2
    PlotObj.y[j] = 5 * prob[j] - 2  
    potential.x[j] = x
# scaled potential to plot
    potential.y[j] = 0.03 * v[j] - 5  
    j = j + 1
# packet deforms with time
for t in range(0, 15000):  
    # while True:
    rate(1000)
    psr[1:-1] = ( psr[1:-1] - (dt / dx2) * (psi[2:] + psi[:-2] - 2 * psi[1:-1]) + dt * v[1:-1] * psi[1:-1] )
    psi[1:-1] = ( psi[1:-1] + (dt / dx2) * (psr[2:] + psr[:-2] - 2 * psr[1:-1]) - dt * v[1:-1] * psr[1:-1] )
# plot the wave packet with time
    PlotObj.y = 4 * (psr**2 + psi**2) - 1  
