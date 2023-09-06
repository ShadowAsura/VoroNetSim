import numpy as np
import matplotlib.pyplot as plt

# Function to generate Mandelbrot fractal
def mandelbrot(c,max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Generate a 2D grid of complex numbers
x, y = np.linspace(-2.0, 1.0, 1000), np.linspace(-1.5, 1.5, 1000)
C = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
C = C[:, 0] + 1j * C[:, 1]

# Compute Mandelbrot set
max_iter = 256
M = np.array([mandelbrot(c,max_iter) for c in C])

# Reshape and normalize the result
M = M.reshape(1000, 1000) / max_iter

# Plot the Mandelbrot set
plt.imshow(M, extent=[-2.0, 1.0, -1.5, 1.5], cmap='inferno')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
