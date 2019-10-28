import matplotlib.pyplot as plt
import numpy as np

def f1(x): 
    '''Define first function'''
    return np.cos(x)

def f2(x): 
    '''Define second function'''
    return np.sin(x)


# Get all but the last point...for reasons
x = np.linspace(0,2*np.pi,100)[:-1]
# Generate our y data as a list of two vectors
y = [f1(x), f2(x)]
# Define the color and linestyle associated with each line
c = ['r-', 'g--']

# Load the data into a single list.
# This is a little overkill for just two lines...
# results in d = [x, y[0], c[0], x, y[1], c[1]]
d = []
for i in range(len(y)):
    d.append(x)
    d.append(y[i])
    d.append(c[i])

# Generate our figure canvas
fig, ax = plt.subplots()
# Extract the line objects
lines = ax.plot(*d)  # Note the missing comma
# Set some lables
ax.set_ylabel('f(x)')
ax.set_xlabel('x')
# Define the legend
ax.legend(['f$_1$(x)', 'f$_2$(x)'], ncol=2, loc=1)
# Define some custom tick labels
ax.set_xticks(np.linspace(0,2*np.pi, 5))
ax.set_xticklabels(['0', '$\\frac{\pi}{2}$', '$\pi$', '$\\frac{3\pi}{2}$', '$2\pi$'])
# Set the limits on our plot
ax.set_xlim(0, 2*np.pi)
# Turn on the interactive plot mode
plt.ion()

# Create an infinite loop...you will have to kill the script to stop it
while True:
    # Go over each line in the figure
    for line in lines:
        # Extract the current data
        y = line.get_ydata()
        # Append the first data point to the end of the data, then truncate the first data point
        y = np.append(y, y[0])[1:]
        # Set the line data to be the new function
        line.set_ydata(y)
    # pause slightly between frames so you can see the plot at all
    plt.pause(0.05)
