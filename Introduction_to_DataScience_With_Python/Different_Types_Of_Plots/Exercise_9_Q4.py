"""
Exercise_9_Q4.py

Purpose:
 - Plot a normalized histogram of gravel radii from a shoeprint sample.
 - Demonstrates bin selection, range restriction, and density normalization in matplotlib.

Expected input:
 - An object or DataFrame named `gravel` with a `radius` attribute or column.
"""

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Plot histogram of gravel radii
# - bins=40: divides data into 40 bins
# - range=(2, 8): restricts histogram to radii between 2 and 8 mm
# - density=True: normalizes histogram so area sums to 1
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label the axes and add a title for clarity
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Show the plot window
plt.show()