import matplotlib
matplotlib.use('Qt5Agg')  # Use 'Qt5Agg' as the backend

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL file
your_mesh = mesh.Mesh.from_file("test.stl")

# Add the cube to the plot
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Set the limits for the axes
axes.set_xlim([your_mesh.x.min(), your_mesh.x.max()])
axes.set_ylim([your_mesh.y.min(), your_mesh.y.max()])
axes.set_zlim([your_mesh.z.min(), your_mesh.z.max()])

# Add grid lines
axes.grid(True)

# Set a reasonable view angle
axes.view_init(elev=20, azim=30)

# Show the plot to the screen
pyplot.show()
