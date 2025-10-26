"""
Plotting_data_with_matplotlib_ex9.py

Short guide:
 - This script visualizes police-department time series for Phoenix, Los Angeles, and Philadelphia.
 - It expects a pandas DataFrame named `data` with columns:
	 'Year', 'Phoenix Police Dept', 'Los Angeles Police Dept', 'Philadelphia Police Dept'
 - If you want to run this file directly, uncomment the sample-data block at the bottom.
"""

# Data handling
import pandas as pd
import numpy as np

# Plotting
import matplotlib.pyplot as plt

# Optional: nicer default styles
plt.style.use('seaborn-darkgrid')   # or 'seaborn' / 'ggplot' as preferred

# ---------------------------------------------------------------------
# NOTE for students:
# The plotting calls below reference a DataFrame named `data`. Before running
# this file as a standalone script make sure `data` is defined (for example
# by loading a CSV with `pd.read_csv(...)`) or use the sample data block
# provided at the end of this file.
# ---------------------------------------------------------------------

# Plot Phoenix values vs Year and set a custom color for clarity.
# - `label="Phoenix"` is used by `plt.legend()` to identify this line.
# - `color="DarkCyan"` accepts any Matplotlib color name or hex code.
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")

# Plot Los Angeles with a dotted line style:
# - `linestyle=":"` produces a dotted line. Alternatives: '-', '--', '-.'.
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=":")

# Plot Philadelphia and display square markers at each datapoint:
# - `marker="s"` uses a square marker. Other markers: 'o', '^', 'x', '+', '*'.
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker="s")

# Add a legend to the plot using the labels we provided above.
plt.legend()

# Show the figure window. In notebooks use `%matplotlib inline` or `%matplotlib notebook`
# to control inline behavior. To save instead of showing, call `plt.savefig("out.png")`.
plt.show()

# ---------------------------------------------------------------------
# Sample data (uncomment to run the file standalone for testing)
# ---------------------------------------------------------------------
# if __name__ == '__main__':
#     np.random.seed(0)
#     years = np.arange(2000, 2010)
#     data = pd.DataFrame({
#         'Year': years,
#         'Phoenix Police Dept': np.random.randint(100, 300, size=len(years)),
#         'Los Angeles Police Dept': np.random.randint(200, 500, size=len(years)),
#         'Philadelphia Police Dept': np.random.randint(50, 250, size=len(years)),
#     })
#     plt.figure(figsize=(10,6))
#     plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color="DarkCyan")
#     plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle=":")
#     plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker="s")
#     plt.xlabel('Year')
#     plt.ylabel('Incidents (sample)')
#     plt.title('Police Dept. Data (sample)')
#     plt.legend()
#     plt.grid(True, alpha=0.3)
#     plt.show()