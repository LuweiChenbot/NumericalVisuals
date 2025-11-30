import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def laplacian1(a, dx):
    return (-2 * a + np.roll(a, 1, axis=0) + np.roll(a, -1, axis=0)) / (dx ** 2)


def laplacian2(a, dx):
    return (-4 * a + np.roll(a, 1, axis=0) + np.roll(a, -1, axis=0) + np.roll(a, 1, axis=1)
            + np.roll(a, -1, axis=1)) / (dx ** 2)


def LaplacianMod(a):
    center = -a
    direct_neighbors = 0.2 * (
            np.roll(a, 1, axis=0)
            + np.roll(a, -1, axis=0)
            + np.roll(a, 1, axis=1)
            + np.roll(a, -1, axis=1)
    )
    diagonal_neighbors = 0.05 * (
            np.roll(np.roll(a, 1, axis=0), 1, axis=1)
            + np.roll(np.roll(a, -1, axis=0), 1, axis=1)
            + np.roll(np.roll(a, -1, axis=0), -1, axis=1)
            + np.roll(np.roll(a, 1, axis=0), -1, axis=1)
    )
    newa = center + direct_neighbors + diagonal_neighbors
    return newa

"""
def random_coeff(shape):
    return (np.random.normal(loc=0, scale=0.05, size=shape),
            np.random.normal(loc=0, scale=0.05, size=shape)
            )
"""

# Calculates one step
def TwoDimensionalEquation(Du, Dv, U, V):
    deltaU = Du * LaplacianMod(U) - U * V ** 2 + alpha * (1 - U)
    deltaV = Dv * LaplacianMod(V) + U * V ** 2 - (alpha + beta) * V
    U += dt * deltaU
    V += dt * deltaV
    return U, V


# Coefficient
size = 128
dx = 1
dt = 0.25
steps = 1
t = 0

Du = 0.5
Dv = 0.27
alpha = 0.057
beta = 0.062

# Plotting
U = np.ones((size, size))
V = np.zeros((size, size))

U[50:60, 50:70] = 1
V[60:80, 70:80] = 1

sum_of_time = 400000
frame = 500
# fig, ax = plt.subplots(nrows=1, ncols=2, figsize = (12,6))


fig = plt.figure()
for t in range(sum_of_time):
    for _ in range(frame):
        U, V = TwoDimensionalEquation(Du, Dv, U, V)
        U, V = U.copy(), V.copy()
    plt.clf()
    plt.imshow(V, cmap="viridis", interpolation="nearest")
    plt.colorbar()
    plt.title(f"Pattern at time={200 * t * dt:4.3f}")
    plt.draw()
    plt.pause(0.0001)




"""
from matplotlib.animation import FuncAnimation
ALL_V = []
for t in range(sum_of_time):
    U += dt * (Du * LaplacianMod(U) - U * (V * V) + alpha * (1 - U))
    V += dt * (Dv * LaplacianMod(V) + U * (V * V) - (alpha + beta) * V)
    ALL_V.append(V.copy())

def update(frame):
    img.set_data(ALL_V[frame * 100])
    plt.title(r"${\rm Pattern\;at}\;t = $" + f"${frame * dt}$")
    return (img,)

fig = plt.figure()
ax: plt.Axes = plt.axes()
img = ax.imshow(V, interpolation="nearest", cmap="viridis")
ani = FuncAnimation(fig, update, frames=400, interval=20, blit=True)
ani.save("test_animation.gif", writer="pillow")
"""




