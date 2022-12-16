""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# ProteinFold.py: Self avoiding random walk
# Stops in corners or  occupied neighbors
# energy  =  -f|eps, f=1 if neighbour = H, f=0 if p
# Yellow dot indicates unconnected neighbor

from vpython import *
import random

Maxx = 500
Maxy = 500
ran = 20
L = 100
m = 100
size = 8
size2 = size * 2
nex = 0
n = 100
M = []
# Arrays for polymer & grid
DD = []  

graph1 = canvas(width=Maxx, height=Maxy, title="Protein Folding", range=ran)
positions = points(color=color.cyan, size=2)


# Select atom's colors
def selectcol():  
# Select H or P
    hp = random.random()  
    if hp <= 0.7:
# Hydrophobic color red
        col = vector(1, 0, 0)  
        r = 2
    else:
# Polar color white
        col = vector(1, 1, 1)  
        r = 1
    return col, r


# Check links energies
def findrest(m, length, fin, fjn):  
    ener = 0
# Next link not considered
    for t in range(m, length + 1):  
        if DD[t][0] == fin and DD[t][1] == fjn and DD[t][2] == 2:
# Red unlinked neighbor
            ener = 1  
    return ener


# Finds energy of each link
def findenergy(length, DD):  
    energy = 0
    for n in range(0, length + 1):
        i = DD[n][0]
        j = DD[n][1]
        cl = DD[n][2]
        if cl == 1:
# if white
            pass  
# red
        else:  
            if n < length + 1:
# Check neighbor i-1,j
                imin = int(i - 1)  
                js = int(j)
                if imin >= 0:
                    e = findrest(n + 2, length, imin, js)
                    energy = energy + e
# Yellow dot at neighbor
                    if e == 1:  
                        xol = 4 * (i - 0.5) - size2
                        yol = -4 * j + size2
                        points(pos=vector(xol, yol,0), color=color.yellow, size=6)
                ima = i + 1
                js = j
# Check neighborr i+1,j
                if ima <= size - 1:  
                    e = findrest(n + 2, length, ima, js)
                    energy = energy + e
# Yellow dot at neighbor
                    if e == 1:  
                        xol = 4 * (i + 0.5) - size2
                        yol = -4 * j + size2
                        points(pos=vector(xol, yol,0), color=color.yellow, size=6)
                iss = i
                jma = j + 1
# Check neighbor i,j+1
                if jma <= size - 1:  
                    e = findrest(n + 2, length, iss, jma)
                    energy = energy + e
# Yellow dot at neighbor
                    if e == 1:  
# Start at middle
                        xol = 4 * i - size2  
                        yol = -4 * (j + 0.5) + size2
                        points(pos=vector(xol, yol,0), color=color.yellow, size=6)
                iss = i
                jmi = j - 1
# Check neighbor i, j-1
                if jmi >= 0:  
                    e = findrest(n + 2, length, iss, jmi)
                    energy = energy + e
# Yellow dot at neighbor
                    if e == 1:  
# Start at middle
                        xol = 4 * i - size2  
                        yol = -4 * (j - 0.5) + size2
                        points(pos=vector(xol, yol,0), color=color.yellow, size=6)
    return energy


# Plot grid
def grid():  
    for j in range(0, size):
# World to screen coord
        yp = -4 * j + size2  
# Horizontal row
        for i in range(0, size):  
            xp = 4 * i - size2
            positions.append(pos=vector(xp, yp,0))


grid()
length = 0
while 1:
    pts2 = label(pos=vector(-5, -18,0), box=0)
    length = 0
    grid = zeros((size, size))
    D = zeros((L, m, n))
    DD = []
# Center of grid
    i = size / 2  
    j = size / 2
    xol = 4 * i - size2
    yol = -4 * j + size2
    col, c = selectcol()
# Particle in center
    grid[i, j] = c  
# Red center
    M = M + [points(pos=vector(xol, yol,0), color=col, size=6)]  
    print(" start     ")
    DD = DD + [[i, j, c]]
    while ( i > 0 and i < size - 1 and j > 0 and j < size - 1 and ( grid[i + 1, j] == 0 or grid[i - 1, j] == 0 or grid[i, j + 1] == 0 or grid[i, j - 1] == 0 ) ):
        r = random.random()
# Probability 25%
        if r < 0.25:  
            if grid[i + 1, j] == 0:
# Step R if empty
                i += 1  
# Step L
        elif 0.25 < r and r < 0.5:  
            if grid[i - 1, j] == 0:
                i -= 1
# Up
        elif 0.50 < r and r < 0.75:  
            if grid[i, j - 1] == 0:
                j -= 1
# Down
        else:  
            if grid[i, j + 1] == 0:
                j += 1
        if grid[i, j] == 0:
            col, c = selectcol()
# Occupy grid point
            grid[i, j] = 2  
# Increase length as occupied
            length += 1  
            DD = DD + [[i, j, c]]
            xp = 4 * i - size2
            yp = -4 * j + size2
# Connect last to new
            curve(pos=[(xol, yol), (xp, yp)])  
            M = M + [points(pos=vector(xp, yp,0), color=col, size=6)]
# Start new line
            xol = xp  
            yol = yp
        while j == (size - 1) and i != 0 and i != (size - 1):
            r1 = random.random()
# Prob 20% move left
            if r1 < 0.2:  
                if grid[i - 1, j] == 0:
                    i -= 1
# Prob 20% move right
            elif r1 > 0.2 and r1 < 0.4:  
                if grid[i + 1, j] == 0:
                    i += 1
# Prob 60% move up
            else:  
                if grid[i, j - 1] == 0:
                    j -= 1
            if grid[i, j] == 0:
# Increase length
                col, c = selectcol()  
# Grid point occupied
                grid[i, j] = 2  
                length += 1
                DD = DD + [[i, j, c]]
                xp = 4 * i - size2
                yp = -4 * j + size2
                curve(pos=[(xol, yol), (xp, yp)])
                M = M + [points(pos=vector(xp, yp,0), color=col, size=6)]
                xol = xp
# Last row; Stop if corner or neighbors
                yol = yp  
            if (i == 0 or i == (size - 1)) or ( grid[i - 1, size - 1] != 0 and grid[i + 1, size - 1] != 0 ):
                break
# First row
        while j == 0 and i != 0 and i != (size - 1):  
            r1 = random.random()
            if r1 < 0.2:
                if grid[i - 1, j] == 0:
                    i -= 1
            elif r1 > 0.2 and r1 < 0.4:
                if grid[i + 1, j] == 0:
                    i += 1
            else:
                if grid[i, j + 1] == 0:
                    j += 1
            if grid[i, j] == 0:
                col, c = selectcol()
                grid[i, j] = 2
                length += 1
                DD = DD + [[i, j, c]]
                xp = 4 * i - size2
                yp = -4 * j + size2
                curve(pos=[(xol, yol), (xp, yp)])
                M = M + [points(pos=vector(xp, yp,0), color=col, size=6)]
                xol = xp
                yol = yp
            if ( i == (size - 1) or i == 0 or (grid[i - 1, 0] != 0 and grid[i + 1, 0] != 0) ):
                break
# First column
        while i == 0 and j != 0 and j != (size - 1):  
            r1 = random.random()
            if r1 < 0.2:
                if grid[i, j - 1] == 0:
                    j -= 1
            elif r1 > 0.2 and r1 < 0.4:
                if grid[i, j + 1] == 0:
                    j += 1
            else:
                if grid[i + 1, j] == 0:
                    i += 1
            if grid[i, j] == 0:
                col, c = selectcol()
                grid[i, j] = c
                length += 1
                DD = DD + [[i, j, c]]
                xp = 4 * i - size2
                yp = -4 * j + size2
                curve(pos=[(xol, yol), (xp, yp)])
                M = M + [points(pos=vector(xp, yp,0), color=col, size=6)]
                xol = xp
                yol = yp
            if ( j == (size - 1) or j == 0 or (grid[0, j + 1] != 0 and grid[0, j - 1] != 0) ):
                break
# Last col
        while i == (size - 1) and j != 0 and j != (size - 1):  
            r1 = random.random()
            if r1 < 0.2:
                if grid[i, j - 1] == 0:
                    j -= 1
            elif r1 > 0.2 and r1 < 0.4:
                if grid[i, j + 1] == 0:
                    j += 1
            else:
                if grid[i - 1, j] == 0:
                    i -= 1
            if grid[i, j] == 0:
                col, c = selectcol()
                grid[i, j] = c
                length += 1
                col, c = selectcol()
                DD = DD + [[i, j, c]]
                xp = 4 * i - size2
                yp = -4 * j + size2
                curve(pos=[(xol, yol), (xp, yp)])
                M = M + [points(pos=vector(xp, yp,0), color=col, size=6)]
                xol = xp
                yol = yp
            if j == (size - 1) or ( grid[size - 1, j + 1] != 0 and grid[size - 1, j - 1] != 0 ):
                break
    label(pos=vector(-10, -18,0), text="Length=", box=0)
    label(pos=vector(10, 18, 0), text="Click for new walk", color=color.red, canvas=graph1)
    pts2.text = "%4s" % length
    label(pos=vector(5, -18, 0), text="Energy", box=0)
# Energy
    evalue = label(pos=vector(10, -18,0), box=0)  
    evalue.text = "%4s" % findenergy(length, DD)
    print(("energy is ", findenergy(length, DD)))
    print("dd")
# Detect mouse click
    graph1.waitfor('click')  
# Start new walk
    for obj in graph1.objects:  
        if obj is positions or obj is curve:
            continue
# Clear curve
        obj.visible = 0  
