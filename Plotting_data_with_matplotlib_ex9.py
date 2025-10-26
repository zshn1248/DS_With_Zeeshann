# Data handling
import pandas as pd
import numpy as np

# Plotting
import matplotlib.pyplot as plt

# Optional: nicer default styles
plt.style.use('seaborn-darkgrid')   # or 'seaborn' / 'ggplot' as preferred
# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=":")

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker="s")

# Add a legend
plt.legend()

# Display the plot
plt.show()