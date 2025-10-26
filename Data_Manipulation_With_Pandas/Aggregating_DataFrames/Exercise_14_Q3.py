# Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index=("type"), columns="is_holiday", aggfunc="mean")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)
 