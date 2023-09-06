import numpy as np
import matplotlib.pyplot as plt

# Initialize celestial bodies
num_bodies = 50  # Number of celestial bodies
np.random.seed(0)  # For reproducibility

# Randomly place points in a 2D space to represent celestial bodies
coordinates = np.random.rand(num_bodies, 2)

# Assign random mass to each celestial body
masses = np.random.rand(num_bodies)

# For demonstration, let's plot the initial positions of the celestial bodies
plt.scatter(coordinates[:, 0], coordinates[:, 1], c=masses, cmap='viridis', s=50)
plt.colorbar(label='Mass')
plt.title('Initial Positions of Celestial Bodies')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.show()
