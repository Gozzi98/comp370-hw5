import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import calendar

# Read the CSV file into a DataFrame
df = pd.read_csv("nyc_311.csv", header=None)

# Assuming that the date-related column is at a specific index, e.g., index 1
date_column_index = 1
complaint_type_index = 2  # Assuming complaint type is in column 2

# Create a dictionary to count complaints by month for each type
complaints_by_month = defaultdict(lambda: defaultdict(int))

for index, row in df.iterrows():
    timestamp = row[date_column_index]
    complaint_type = row[complaint_type_index]
    
    # Extract the month from the timestamp
    try:
        month = pd.to_datetime(timestamp).month
        complaints_by_month[complaint_type][month] += 1
    except ValueError:
        # Handle any potential parsing errors with invalid date formats
        pass

# Sort the months for correct plotting
sorted_months = sorted(list(complaints_by_month.values())[0].keys())

# Map the numeric month representations to their names
month_names = [calendar.month_name[month] for month in sorted_months]
# Create separate line plots for each complaint type
for complaint_type, counts in complaints_by_month.items():
    complaint_counts = [counts[month] for month in sorted_months]
    plt.plot(month_names, complaint_counts, marker='o', linestyle='-', label=complaint_type)

# Configure plot settings
plt.xlabel('Month')
plt.ylabel('Number of Complaints')
plt.title('Complaints by Month Throughout the Year')
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))  # Place legend outside the plot
plt.tight_layout()  # Ensure the legend is displayed properly

# Show the combined plot with separate lines for each complaint type
plt.show()