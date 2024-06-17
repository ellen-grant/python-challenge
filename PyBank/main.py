import os
import csv


budget_data_path = '/Users/ellengrant/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv'



# Initialize lists to store data
dates = []
profits_losses = []

# Read the CSV file
with open(budget_data_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Calculate the total number of months included in the dataset
total_months = len(dates)

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = sum(profits_losses)

# Calculate the changes in "Profit/Losses" over the entire period and then the average of those changes
changes = [profits_losses[i] - profits_losses[i - 1] for i in range(1, total_months)]
average_change = sum(changes) / len(changes)

# Identify the greatest increase in profits (date and amount) over the entire period
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]

# Identify the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

# Prepare the results
analysis_results = {
    "Total Months": total_months,
    "Net Total": net_total,
    "Average Change": average_change,
    "Greatest Increase": (greatest_increase_date, greatest_increase),
    "Greatest Decrease": (greatest_decrease_date, greatest_decrease)
}

# Print the results
for key, value in analysis_results.items():
    print(f"{key}: {value}")