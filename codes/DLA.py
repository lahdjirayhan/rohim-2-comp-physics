# DLA.py: Diffusion limited aggregation

from vpython import *
import numpy as np
import random

# Canvas width, height
Maxx, Maxy = 500, 500

escene = canvas(
    width=Maxx, height=Maxy, title="Diffusion Limited Aggregation", range=40
)
escene.center = vector(0, 0, 15)


def gauss_ran():
    r1 = random.random()
    r2 = random.random()
    fac = np.sqrt(-2 * np.log(r1))
    mem = int(fac * 20_000 * np.cos(2 * np.pi * 2))
    return mem


rad = 40.0
step = 0
trav = 0
size = 60
max = 500
# Particle locations, 1=occupied
grid = np.zeros((size, size))
ring(
    pos=vector(0, 0, 0),
    axis=vector(0, 0, 1),
    radius=rad,
    thickness=0.5,
    color=color.green,
)
# Moving ball
ball = sphere(radius=0.8)

while True:
    hit = 0
    angle = 2.0 * np.pi * random.random()
    x = rad * np.cos(angle)
    y = rad * np.sin(angle)
    dist = abs(gauss_ran())
    # Uncomment to see start point
    # print(dist)
    # sphere(pos=vector(x,y,0), color=color.magenta)
    trav = 0

    while hit == 0 and (-40 < x < 40) and (-40 < y < 40) and trav < abs(dist):
        if random.random() < 0.5:
            step = 1
        else:
            step = -1

        # Transform coord for indexes
        # xg = m*x+b, 30 = 0*m+b, 58=m*40+b
        xg = int(0.7 * x + 30)
        yg = int(-0.7 * y + 30 + 0.5)
        if (
            grid[xg + 1, yg] + grid[xg - 1, yg] + grid[xg, yg + 1] + grid[xg, yg - 1]
        ) > -1:
            # Ball hits fixed ball,
            # Position is now occupied
            hit = 1
            grid[xg, yg] = 1
            sphere(pos=vector(x, y, 0), radius=0.8, color=color.yellow)
        else:
            # Probability 1/2 to move either right or up
            if random.random() < 0.5:
                x += step
            else:
                y += step

            xp = 80 * x / 56.0 - 40
            yp = -80 * y / 56.0 + 40
            ball.pos = vector(xp, yp, 0)

        # Change ball speed
        rate(10)

        # Increments distance, < dist
        trav += 1
