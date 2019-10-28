import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

# Set the size of the arrays to solve
N = 30
dx = 1.0 / N
S = 100
x = np.linspace(0, 1, N)
y = x.copy()
X, Y = np.meshgrid(x, y)
# Define the starting array and boundary condition values
T = np.zeros((N,N))

def update_T(T):
    '''
    Solve Poisson's equation: d^2T/dx^2 + d^2T/dy^2 = S
    Used backward difference formula to solve for T_{i,j}
    '''
    yield T  # Fancy return that starts the next function from here
    while True: # Start convergence loop
        for i in range(1,N-1):  # loop over x values, skipping boundaries
            for j in range(1,N-1):  # loop over y values, skipping boundaries
                # solve for current cell
                T[i,j] = 0.25*(T[i+1,j]+T[i-1,j]+T[i,j+1]+T[i,j-1]+ S * dx**2)
        yield T  # Fancy return that starts the next function from here
    
def updatefig(frame_number, generator, plot):
    '''Function that is called to update the figure'''
    # Get the next set of data using the generator
    T = next(generator)
    # Create a new plot and send it back to the animator
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, T, linewidth=0.2, antialiased=True, vmin=0, vmax=5, cmap='magma')
    plot[0]._facecolors2d = plot[0]._facecolors3d
    plot[0]._edgecolors2d = plot[0]._edgecolors3d
    return plot

# Create the plotting figure
fig = plt.figure()
# Set up the axis for 3D plot
ax = p3.Axes3D(fig)

# Create the generator that will give the next set of temperatures
# Think of a generator as a list that can only give you the next item (like range)
generator = update_T(T)

# Create our surface plot
plot = [ax.plot_surface(X, Y, T, linewidth=0.2, antialiased=True, vmin=0, vmax=5, cmap='magma')]
# Set the limits of the z axis
ax.set_zlim(0, 5)
# These are needed to fix a bug in matplotlib 3D plots
plot[0]._facecolors2d = plot[0]._facecolors3d
plot[0]._edgecolors2d = plot[0]._edgecolors3d

# Start the animator
# Notice the fargs argument that lets us give arguments to the update function
anim = animation.FuncAnimation(fig, updatefig, fargs=(generator, plot), repeat=True, interval=1)
plt.show()

