""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# LaplaceTri.py: Soltn Laplace Eqtn for field in triangular capacitor

import matplotlib.pylab as p
from mpl_toolkits.mplot3d import Axes3D
from numpy import *

i = 0
x = 0.0
y = 0.3
a1 = -0.5
b1 = -0.433
a2 = 0.5
b2 = -0.433
a3 = 0.0
b3 = 0.433
Nmax = 100
Niter = 100
V = zeros((Nmax, Nmax), float)
grid = ones((Nmax, Nmax))
sq3 = sqrt(3.0)
y0 = -sq3 / 4.0


# Potential on one side
def contour():
    # Rows
    for i in range(0, 100):
        # Columns
        for j in range(0, 100):
            if i == 0:
                V[0, j] = 1000


# Set interior grid points to 0
for i in range(0, 100):
    y = y0 + i * 0.01
    x0 = -0.5
    for j in range(0, 100):
        x = x0 + j * 0.01
        eps = 0.006
        if (y <= sq3 * (x + 0.25) and x < 0.0) or (y < -sq3 * (x - 0.25) and x >= 0):
            grid[i, j] = 0
        else:
            if y <= sq3 / 4.0 + 0.01:
                # Triangle tip
                V[i, j] = 0.0
# Iterate
for iter in range(1, Niter):
    if iter % 50 == 0:
        print(("Working, iteration", iter, "out of", Niter))
    # keep one side at 1000V
    contour()
    for i in range(1, Nmax - 2):
        for j in range(1, Nmax - 2):
            # interior points
            if grid[i, j] == 0.0:
                V[i, j] = 0.25 * (V[i + 1, j] + V[i - 1, j] + V[i, j + 1] + V[i, j - 1])
x = list(range(0, Nmax - 1, 2))
# Plot every other point
y = list(range(0, Nmax, 2))
X, Y = p.meshgrid(x, y)


# Function returns V(x, y)
def functz(V):
    z = V[X, Y]
    return z


Z = functz(V)
# Create figure
fig = p.figure()
# Plot axes
ax = fig.add_subplot(111, projection="3d")
# Red wireframe
ax.plot_wireframe(X, Y, Z, color="r")
ax.set_title("Potential within Triangle (Rotatable)")
# Label axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Potential")
# Display fig
p.show()
