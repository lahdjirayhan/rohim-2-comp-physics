# Column.py: Correlated ballistic deposition

from vpython import *
import random
import numpy as np

graph1 = canvas(
    width=500, height=500, title="Correlated Ballistic Deposition", range=250
)

pts = points(color=color.green, radius=1)
hit = np.zeros((200))

maxi = 80_000
npoints = 200
dist = 0
oldx, oldy = 100, 0

for i in range(maxi):
    r = int(npoints * random.random())
    x = r - oldx
    y = hit[r] - oldy
    dist = x * x + y * y

    prob = 9.0 / dist

    pp = random.random()

    if pp < prob:
        if r > 0 and r < (npoints - 1):
            if hit[r] >= hit[r - 1] and hit[r] >= hit[r + 1]:
                hit[r] = hit[r] + 1
            else:
                if hit[r - 1] > hit[r + 1]:
                    hit[r] = hit[r - 1]
                else:
                    hit[r] = hit[r + 1]

        oldx = r
        oldy = hit[r]

        olxc = oldx * 2 - 200
        olyc = oldy * 4 - 200

        pts.append(pos=vector(olxc, olyc, 0))

while True:
    rate(60)
