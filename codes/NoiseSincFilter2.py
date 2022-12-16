""" From "COMPUTATIONAL PHYSICS" & "COMPUTER PROBLEMS in PHYSICS"
    by RH Landau, MJ Paez, and CC Bordeianu (deceased)
    Copyright R Landau, Oregon State Unv, MJ Paez, Univ Antioquia, 
    C Bordeianu, Univ Bucharest, 2017. 
    Please respect copyright & acknowledge our work."""

# NoiseSyncFilter2.py: Noise removal wi Sinc Filter

from numpy import *
import random

N = 512
imax = 512
maxnoise = 20

fg = zeros((N + 1, N + 1), float)
fnoi = zeros((N + 1, N + 1), float)
y = zeros((N + 1, N + 1), float)

# Input image
Input = open("Mariana.dat", "r")  
Marnoi = open("MarianaNoise.pgm", "w+t")
Out = open("Mariana.pgm", "w+t")
Clean = open("MarianaCleand.pgm", "w+t")

# Netpbm internal image code
Marnoi.write("P2\n")  
# Pixel dimensions of image
Marnoi.write("512  512\n")  
# Byte scale, 255=white.
Marnoi.write("255\n")  
Out.write("P2\n")
Out.write("512  512\n")
Out.write("255\n")
Clean.write("P2\n")
Clean.write("512  512\n")
Clean.write("255\n")


# Low-pass windowed-sinc filter
def filter():  
    h = zeros((imax), float)
# Filter length (101 points)
    m = 100  
    fc = 0.07
# Low-pass filter kernel
    for i in range(0, 100):  
        if (i - (m // 2)) == 0:
            h[i] = 2 * math.pi * fc
        if (i - (m // 2)) != 0:
            h[i] = sin(2 * math.pi * fc * (i - m / 2)) / (i - m / 2)
# Hamming window
        h[i] = h[i] * (0.54 - 0.46 * cos(2 * math.pi * i / m))  
# Normalize low-pass filter kernel
    sum = 0.0  
    for i in range(0, 100):
        sum = sum + h[i]
    for i in range(0, 100):
        h[i] = h[i] / sum
    for j in range(0, imax):
        if j % 100 == 0:
            print(("Waiting till reach 500, now at: ", j))
# Convolute input with filter
        for k in range(0, imax):  
            y[k, j] = 0
            for i in range(0, 100):
                if k > 99:
                    y[k, j] = y[k, j] + fnoi[k - i, j] * h[i]
# Partially filtered
            Clean.write("%4d" % (int(y[k, j])))  
        Clean.write("\n")


for j in range(0, N):
    for i in range(0, N):
        fg[i, j] = int(Input.readline())
# Signal + noise
        fnoi[i, j] = fg[i, j] + maxnoise * (2 * random.random() - 1)  
# Output in rows
for j in range(0, N):  
    for i in range(0, N):
        Marnoi.write("%4d" % (int(fnoi[i, j])))
        Out.write("%4d" % (int(fg[i, j])))
    Marnoi.write("\n")
    Out.write("\n")
Marnoi.closed
Out.closed
Input.closed
Clean.closed
list(filter())
print("MarianaCleaned written to disk\n All Done!")
