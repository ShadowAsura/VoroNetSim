from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np

# Generate random points as Voronoi seeds
# For demonstration, we'll use 20 random points in a 2D space
np.random.seed(0)  # For reproducibility
points = np.random.rand(20, 2)  # 20 points in 2D

# Compute Voronoi Diagram
# The Voronoi function from scipy.spatial computes the Voronoi diagram for us
vor = Voronoi(points)

# Plot Voronoi Diagram
# voronoi_plot_2d is a utility function that helps us visualize the Voronoi diagram
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax)

# Annotate seed points
# This will help us identify the seed point associated with each Voronoi cell
for i, point in enumerate(points):
    plt.text(point[0], point[1], f"{i}")

# Show plot
plt.show()
