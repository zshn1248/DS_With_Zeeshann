# Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)