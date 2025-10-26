# Get the mean and median of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales", index="type", aggfunc=["mean", "median"])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)
