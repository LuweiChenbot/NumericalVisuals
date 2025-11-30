import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
rh = (10*(10+3+(8/3)))/(10-(8/3)-1)
def lorenz(xyz, *, s=10, r=rh+0.00000000000001, b=8.0 / 3.0):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Point of interest in three-dimensional space.
    s, r, b : float
       Parameters defining the Lorenz attractor.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Values of the Lorenz attractor's partial derivatives at *xyz*.
    """
    x, y, z = xyz
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])

# Parameters
dt = 0.01
num_steps = 10000
xyzs = np.empty((num_steps + 1, 3))  # Array to store points
xyzs[0] = (np.sqrt((8/3) * (rh - 1))+0.000000005, np.sqrt((8/3) * (rh - 1)),
           rh - 1)  # Initial values
# Compute all points in advance
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlim((-20, 20))
ax.set_ylim((-30, 30))
ax.set_zlim((0, 50))
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

# Initialize line and time step text
line, = ax.plot([], [], [], lw=0.5)
time_text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes, fontsize=12)

# Function to update the animation
def update(num):
    # Update line
    line.set_data(xyzs[:num, 0], xyzs[:num, 1])
    line.set_3d_properties(xyzs[:num, 2])
    # Update time step text
    time_text.set_text(f"Time: {num * dt:.2f} seconds")
    return line, time_text

# Create animation
ani = FuncAnimation(fig, update, frames=num_steps, interval=10, blit=True)

# Show the animation
plt.show()
