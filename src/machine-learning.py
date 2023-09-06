from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data for demonstration
# Let's assume a simple linear relationship: y = 2x + 1
np.random.seed(0)  # For reproducibility
X = 2 * np.random.rand(100, 1)  # Random dataset of 100 points
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3x + Gaussian noise

# Create a Linear Regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Make predictions
X_new = np.array([[0], [2]])
y_predict = model.predict(X_new)

# Plot the data and the model prediction
plt.scatter(X, y, label='Data Points')
plt.plot(X_new, y_predict, 'r-', label='Prediction')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
