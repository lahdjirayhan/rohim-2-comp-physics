""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia,
    C Bordeianu, Univ Bucharest, 2017.
    Please respect copyright & acknowledge our work."""

# SolitonAnimate.py: Solves KdeV equation for a soliton

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ds = 0.4
dt = 0.1
mu = 0.1
eps = 0.2
mx = 101
fac = mu * dt / (ds**3)
u = np.zeros((mx, 3), float)  # Soliton amplitude
maxtime = 2500


def init():
    for i in range(0, mx):
        u[i, 0] = 0.5 * (
            1
            - (
                (np.exp(2 * (0.2 * ds * i - 5)) - 1)
                / (np.exp(2 * (0.2 * ds * i - 5)) + 1)
            )
        )

    u[0, 1] = 1
    u[0, 2] = 1
    u[mx - 1, 1] = 0
    u[mx - 1, 2] = 0


init()

k = range(0, mx)
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, mx), ylim=(0, 3))
ax.grid()
plt.ylabel("Height")
plt.title("Soliton (runs very slowly)")
line, *_ = ax.plot(k, u[k, 0], "b", linewidth=2)
time = ax.annotate(0, xy=(ax.get_xlim()[0], ax.get_ylim()[1]), ha="left", va="top")

# First time step
for i in range(1, mx - 1):
    a1 = eps * dt * (u[i + 1, 0] + u[i, 0] + u[i - 1, 0]) / (ds * 6)
    if i > 1 and i < mx - 2:
        a2 = u[i + 2, 0] + 2 * u[i - 1, 0] - 2 * u[i + 1, 0] - u[i - 2, 0]
    else:
        a2 = u[i - 1, 0] - u[i + 1, 0]
    a3 = u[i + 1, 0] - u[i - 1, 0]
    u[i, 1] = u[i, 0] - a1 * a3 - fac * a2 / 3

# Later time steps

# Following next time steps
def animate(num):
    for i in range(1, mx - 2):
        a1 = eps * dt * (u[i + 1, 1] + u[i, 1] + u[i - 1, 1]) / (3 * ds)
        if i > 1 and i < mx - 2:
            a2 = u[i + 2, 1] + 2 * u[i - 1, 1] - 2 * u[i + 1, 1] - u[i - 2, 1]
        else:
            a2 = u[i - 1, 1] - u[i + 1, 1]
        a3 = u[i + 1, 1] - u[i - 1, 1]
        u[i, 2] = u[i, 0] - a1 * a3 - 2 * fac * a2 / 3

    # Plot (position, height)
    line.set_data(k, u[k, 2])
    time.set_text(str(num))

    # Recycle array
    u[k, 0] = u[k, 1]
    u[k, 1] = u[k, 2]
    return (line,)


ani = animation.FuncAnimation(fig, animate, maxtime, interval=30, repeat=False)
plt.show()
print("finished")
