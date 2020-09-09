import os
import csv

# Get the Data from the CSV file in the resources folder
Budget_csv = os.path.join("Resources", "budget_data.csv")

# Open the file using write mode while holding the contents in the correct file
with open(Budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    # Skip the header row
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    # Find the total number of months
    length_months = len(months)

# Append the values to the correct rows for months and the total profit
total_months = []
total_profit = []

for rows in csvreader:
    total_months.Append(row[0])
    total_profit.Append(int(row[1]))

# Find the change in revenue
revenue_change = []

for x in range(1, len(total_profit)):
    revenue_change.Append((int(total_profit[x]) - int(total_profit[x-1])))
    
# Calculate the average
    revenue_average = []
    revenue_average = sum(revenue_change) / len(revenue)
    
#Calculate the greatest increase in profits over the entire period
    greatest_increase = max(revenue_change)
# Calculate the greatest decrease in profits over the entire period
    greatest_decrease = min(revenue_change)

# Print the analysis
    print("Financial Analysis")
    print("..................................")
    print("Total months: " + str(total_months))
    print("Total: " + "$" + str(sum(total_profit)))
    print("Average change: " + "$" + str(revenue_average))
    print("Greatest increase in profits: " + "str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest decrease in profits: " + "str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))
