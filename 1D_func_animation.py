import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    # Function to move
    return np.sin(x)

# Original data points
x = np.linspace(0, 2 * np.pi, 120)

# Create a figure object
fig = plt.figure()
# Get the axis for the figure
ax = fig.add_subplot(111)
# Get the line from the plot
line1, = ax.plot(x, f(x), 'g-')  # note the comma

# Add a static line to the plot
line2, = ax.plot(x, f(x), 'r--')  # note the comma

def updatefig(*args):
    '''Update the data after a shift in x points'''
    # Shift the x points
    global x
    x += np.pi / 15.

    # Update the data on the plot
    line1.set_ydata(f(x))

    # Redraw the plot
    fig.canvas.draw()

    return line1,  # note the comma

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
ani.save('name.mp4', writer='ffmpeg')
plt.show()
