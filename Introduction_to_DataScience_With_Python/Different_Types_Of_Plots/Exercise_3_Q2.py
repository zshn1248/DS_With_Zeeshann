"""
Exercise_3_Q2.py

Purpose:
 - Plot cellphone location data as a scatter plot with square markers.
 - Demonstrates marker customization and axis labeling in matplotlib.

Expected input:
 - An object or DataFrame named `cellphone` with attributes or columns `x` (Longitude) and `y` (Latitude).
"""

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Plot cellphone locations as red squares
# - marker="s" sets square markers
# - color='red' colors all points red
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker="s")

# Label the axes for clarity
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Show the plot window
plt.show()