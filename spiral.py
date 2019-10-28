import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def get_xy(t):
    '''create a function for the data'''
    a = 0.15
    b = 0.03
    x = a * np.cos(t)*np.exp(b*np.linspace(0,150,1000))
    y = a * np.sin(t)*np.exp(b*np.linspace(0,150,1000))
    return x, y
    
def updatefig(*args):
    '''create a function to update the plot data'''
    # Allow editing t from within the function
    global t
    # Increas the time by one
    t += 1
    # recompute the plot data
    x, y = get_xy(t)
    # set the plot datas
    line.set_xdata(x)
    line.set_ydata(y)
    # redraw the plot
    fig.canvas.draw()
    return line,  # notice the comma
    
# Define our initial vector
t = np.linspace(0,40,1000)
# Compute the initial data
x, y = get_xy(t)
    
# Create a plot canvas
fig = plt.figure()
# Get the axis for the canvas
ax = fig.add_subplot(111)
# Define the axis limits
ax.axis([-10,10,-10,10])
# Create the plot
line, = ax.plot(x, y)  # notice the comma
    
# Create an animation
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
