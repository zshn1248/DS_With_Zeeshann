"""
Exercise_8_Q3.py

Purpose:
 - Plot a histogram of puppy weights, focusing on the range 5 to 35 lbs.
 - Demonstrates histogram range selection and axis labeling in matplotlib.

Expected input:
 - An object or DataFrame named `puppies` with a `weight` attribute or column.
"""

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Plot histogram of puppy weights
# - range=(5, 35) restricts the histogram to weights between 5 and 35 lbs
plt.hist(puppies.weight,
        range=(5, 35))

# Label the axes for clarity
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Show the plot window
plt.show()