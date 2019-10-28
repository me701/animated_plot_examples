import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d

def get_xy(t):
    '''Define a function to plot'''
    a = 0.5
    b = 0.05
    x = a * np.cos(t)*np.exp(b*t)
    y = a * np.sin(t)*np.exp(b*t)
    return x, y
    
def updatefig(*args):
    '''Function that is called to update the figure'''
    global t_max
    t_max += 1
    x, y = get_xy(np.linspace(0,t_max,1000))
    line.set_xdata(x)
    line.set_ydata(y)
    fig.canvas.draw()
    return line,  # note the comma
    
# Get our initial data for the figure
t_max = 0
x, y = get_xy(np.linspace(0,t_max,1000))
    
# Create our figure axis
fig, ax = plt.subplots()
ax.axis([-10,10,-10,10])
line, = ax.plot(x, y)
    
# Animate our figure using FuncAnimation
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True, save_count=100)
# save_count is the number of frames to write to the file
ani.save('name.mp4', writer='ffmpeg')
# The show picks up where the save left off
plt.show()
