from numpy import array, arange, fromfunction, flip, zeros, vectorize, exp
from sympy import isprime, primerange
import matplotlib.pyplot as plt

import sys
import os
os.chdir(os.path.join(os.path.dirname(__file__)))

def ulam_square(n):
    if n == 0:
        square = array([[1]])
    else:
        o = 2*n + 1

        bottom  = arange(o**2 - 1*o + 1, o**2 - 0*o + 1)
        left    = arange(o**2 - 2*o + 2, o**2 - 1*o + 2)
        top     = arange(o**2 - 3*o + 3, o**2 - 2*o + 3)
        right   = arange(o**2 - 4*o + 4, o**2 - 3*o + 4)

        square = zeros((o, o), dtype=int)
        square[:, o-1]  = flip(right)
        square[0, :]    = flip(top)
        square[:, 0]    = left
        square[o-1, :]  = bottom

        square[1:o-1, 1:o-1] = ulam_square(n-1)
    return square

def run():
    GRID_SIZE = 250
    sys.setrecursionlimit(GRID_SIZE * 2)

    Z = vectorize(isprime)(ulam_square(GRID_SIZE))

    fig, ax = plt.subplots()
    ax.axis('off')
    ax.imshow(Z, cmap='gray')
    fig.savefig('assets/ulam.png', bbox_inches='tight', pad_inches=0)

    # --------------------------------- Extension -------------------------------- #

    N = 10_000

    pts = fromfunction(lambda n: n*exp(n*1j), (N,))
    pts = pts[list(primerange(N))]

    fig, ax = plt.subplots()
    ax.axis('off')
    plt.scatter(pts.real, pts.imag, s=1, c='black')
    fig.savefig('assets/polar.png')

if __name__ == '__main__':
    run()
