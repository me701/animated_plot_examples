import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x, y, t):
    return (np.cos(x) + np.cos(y)) * np.cos(t)

def time_dep(f, x, y):
    data = []
    for t in np.linspace(0.0, 2 * np.pi, 200):
        data.append(f(x, y, t))
    return np.array(data)

# Generate some random data
x = np.linspace(-5 * np.pi, 5 * np.pi, 200)
y = x.copy()
X, Y = np.meshgrid(x, y)

data = time_dep(f, X, Y)

# Create our main figure
fig = plt.figure()

# Create a list of plot images
im = []
for i in range(len(data)):
    plot = plt.pcolormesh(X, Y, data[i], vmin=-1, vmax=1)
    im.append((plot,))
    
# Each plot is now a frame in the image
ani = animation.ArtistAnimation(fig, im, interval=50, blit=True)
# Save the figure
ani.save('name.mp4', writer='ffmpeg')
# Show the outcome
plt.show()
