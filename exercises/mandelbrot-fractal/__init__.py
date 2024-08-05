from numpy import linspace, meshgrid, vectorize
import matplotlib.pyplot as plt

import os
os.chdir(os.path.join(os.path.dirname(__file__)))

# Set these higher for increased accuracy
N_MAX = 1000
TOL = 1e16

def func(c):
    return lambda z: z**2 + c
def is_bounded(c):
    f = func(c)

    z = 0
    for _ in range(N_MAX):
        z = f(z)
        if abs(z) > TOL:
            return False
    return True

def run():
    # Set this higher for increased resolution
    GRID_SIZE = 1000

    X, Y = meshgrid(linspace(-2, +2, GRID_SIZE), linspace(-2, +2, GRID_SIZE))
    Z = vectorize(is_bounded)(X + 1j*Y)

    fig, ax = plt.subplots()
    ax.imshow(Z)
    fig.savefig('assets/mandelbrot.png')

if __name__ == '__main__':
    run()
