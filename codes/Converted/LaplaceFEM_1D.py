"""Dirichlet boundary conditions surrounding four walls 
 Domain dimensions: WxH, with 2 triangles per square  
 Based on FEM2DL_Box Matlab program in Polycarpou, Intro to the Finite 
 Element Method in Electromagnetics, Morgan & Claypool (2006) """


# LaplaceFEM_1D.py:  Solutn 1-D Laplace Eq via finite elements; utf8 coding

from visual import *
from visual.graph import *
from numpy import *
from numpy.linalg import solve

N = 11
h = 1.0 / (N - 1)
u = zeros(N, float)
A = zeros((N, N), float)
b = zeros((N, N), float)
x2 = zeros(21, float)
u_fem = zeros(21, float)
u_exact = zeros(21, float)
error = zeros(21, float)
x = zeros(N, float)

graph1 = graph( width=500, height=500, title="Analytic (Blue) vs FEM", xtitle="x", ytitle="U", xmax=1, ymax=1, xmin=0, ymin=0, )
funct1 = gcurve(color=color.blue)
funct2 = gdots(color=color.red)
funct3 = gcurve(color=color.cyan)

for i in range(0, N):
    x[i] = i * h
# Initialize
for i in range(0, N):  
    b[i, 0] = 0.0
    for j in range(0, N):
        A[i][j] = 0.0


# Hat func
def lin1(x, x1, x2):  
    return (x - x1) / (x2 - x1)


def lin2(x, x1, x2):
    return (x2 - x) / (x2 - x1)


def f(x):
    return 1.0


# Simpson
def int1(min, max):  
    no = 1000
    sum = 0.0
    interval = (max - min) / (no - 1)
# Loop odd points
    for n in range(2, no, 2):  
        x = interval * (n - 1)
        sum += 4 * f(x) * lin1(x, min, max)
# Loop even points
    for n in range(3, no, 2):  
        x = interval * (n - 1)
        sum += 2 * f(x) * lin1(x, min, max)
    sum += f(min) * lin1(min, min, max) + f(max) * lin1(max, min, max)
    sum *= interval / 6.0
    return sum


# Simpson
def int2(min, max):  
    no = 1000
    sum = 0.0
    interval = (max - min) / (no - 1)
# Loop odd points
    for n in range(2, no, 2):  
        x = interval * (n - 1)
        sum += 4 * f(x) * lin2(x, min, max)
# Loop even points
    for n in range(3, no, 2):  
        x = interval * (n - 1)
        sum += 2 * f(x) * lin2(x, min, max)
    sum += f(min) * lin2(min, min, max) + f(max) * lin2(max, min, max)
    sum *= interval / 6.0
    return sum


def numerical(x, u, xp):
# Interpolate solution
    N = 11  
    y = 0.0
    for i in range(0, N - 1):
        if xp >= x[i] and xp <= x[i + 1]:
            y = lin2(xp, x[i], x[i + 1]) * u[i] + lin1(xp, x[i], x[i + 1]) * u[i + 1]
    return y


# Analytic solution
def exact(x):  
    u = -x * (x - 3.0) / 2.0
    return u


for i in range(1, N):
    A[i - 1, i - 1] = A[i - 1, i - 1] + 1.0 / h
    A[i - 1, i] = A[i - 1, i] - 1.0 / h
    A[i, i - 1] = A[i - 1, i]
    A[i, i] = A[i, i] + 1.0 / h
    b[i - 1, 0] = b[i - 1, 0] + int2(x[i - 1], x[i])
    b[i, 0] = b[i, 0] + int1(x[i - 1], x[i])

# Dirichlet BC left end
for i in range(1, N):  
    b[i, 0] = b[i, 0] - 0.0 * A[i, 0]
    A[i, 0] = 0.0
    A[0, i] = 0.0
A[0, 0] = 1.0
b[0, 0] = 0.0

# Dirichlet BC right end
for i in range(1, N):  
    b[i, 0] = b[i, 0] - 1.0 * A[i, N - 1]
    A[i, N - 1] = 0.0
    A[N - 1, i] = 0.0
A[N - 1, N - 1] = 1.0
b[N - 1, 0] = 1.0
sol = solve(A, b)

for i in range(0, N):
    u[i] = sol[i, 0]

for i in range(0, 21):
    x2[i] = 0.05 * i

for i in range(0, 21):
    u_fem[i] = numerical(x, u, x2[i])
    u_exact[i] = exact(x2[i])
    funct1.plot(pos=(0.05 * i, u_exact[i]))
    funct2.plot(pos=(0.05 * i, u_fem[i]))
# Global error
    error[i] = u_fem[i] - u_exact[i]  