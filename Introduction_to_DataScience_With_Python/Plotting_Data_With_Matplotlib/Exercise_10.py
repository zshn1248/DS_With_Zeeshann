"""
Exercise_10.py

Short guide / classroom notes:
 - This exercise plots three time series (Phoenix, Los Angeles, Philadelphia) versus Year.
 - The plotting code expects a pandas DataFrame named `data` with columns:
	 'Year', 'Phoenix Police Dept', 'Los Angeles Police Dept', 'Philadelphia Police Dept'
 - If you want to run this file directly (for testing), uncomment the sample-data block at the bottom.
"""

# Data handling imports (used if you load or create DataFrames)
import pandas as pd
import numpy as np

# Plotting import
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# Plot style
# - Matplotlib includes a few built-in styles. 'fivethirtyeight' gives a clean
#  , publication-like look. Other options: 'seaborn', 'ggplot', 'classic'.
plt.style.use("fivethirtyeight")

# ---------------------------------------------------------------------
# Plotting calls
# - Each plt.plot(x, y, ...) call draws one line on the current axes.
# - label= sets the legend text for that line (shown when calling plt.legend()).
# - Common visual parameters:
#     color= (e.g. 'C0', '#1f77b4', or named colors), linestyle= ("-", "--", ":"),
#     marker= (e.g. 'o', 's', '^'), linewidth=, alpha= for transparency.
#
# Note: `data` must be defined before these calls (e.g., loaded via pd.read_csv).
# If `data` is missing you will get a NameError; see the sample-data block below.
# ---------------------------------------------------------------------

# Plot Phoenix (default solid line). We add a label for the legend.
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")

# Plot Los Angeles (default style here, but could use linestyle=':' for dotted)
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")

# Plot Philadelphia (again default line; markers could be added with marker='s' etc.)
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend to identify the lines. You can pass loc= to control position
# e.g. plt.legend(loc='upper left') or plt.legend(fontsize='small').
plt.legend()

# Display the plot window (or inline in notebooks). To save to a file instead,
# call plt.savefig('exercise10.png', bbox_inches='tight') before plt.show().
plt.show()

# ---------------------------------------------------------------------
# Sample data / quick test (uncomment to run this file standalone)
# ---------------------------------------------------------------------
# if __name__ == '__main__':
#     # Create small synthetic dataset for testing the plotting calls
#     np.random.seed(1)
#     years = np.arange(2005, 2015)
#     data = pd.DataFrame({
#         'Year': years,
#         'Phoenix Police Dept': np.random.randint(100, 300, size=len(years)),
#         'Los Angeles Police Dept': np.random.randint(200, 500, size=len(years)),
#         'Philadelphia Police Dept': np.random.randint(50, 250, size=len(years)),
#     })
#     # Optionally adjust figure size and labels for nicer output in tests
#     plt.figure(figsize=(10, 6))
#     plt.style.use("fivethirtyeight")
#     plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
#     plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
#     plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")
#     plt.xlabel('Year')
#     plt.ylabel('Incidents (sample)')
#     plt.title('Exercise 10 — Police Dept Trends (sample)')
#     plt.legend()
#     plt.grid(True, alpha=0.3)
#     plt.show()