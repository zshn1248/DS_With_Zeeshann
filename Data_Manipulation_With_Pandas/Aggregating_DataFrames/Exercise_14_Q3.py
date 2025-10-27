"""
Exercise_14_Q3.py

Purpose:
 - Calculate the mean of weekly sales grouped by store type and holiday status using pandas pivot_table.
 - Print the resulting summary table for analysis.

Expected input:
 - A pandas DataFrame named `sales` with columns:
	 'weekly_sales', 'type', 'is_holiday'
"""

# Import pandas for data manipulation
import pandas as pd

# Example: if you have a CSV, load it like this
# sales = pd.read_csv('sales.csv')

# Pivot for mean weekly_sales by store type and holiday
# - values="weekly_sales": the data to aggregate
# - index="type": rows grouped by store type
# - columns="is_holiday": separate columns for holiday/non-holiday
# - aggfunc="mean": compute the mean for each group
mean_sales_by_type_holiday = sales.pivot_table(
	values="weekly_sales",
	index="type",
	columns="is_holiday",
	aggfunc="mean"
)

# Print the resulting pivot table
print(mean_sales_by_type_holiday)
 