import os
import csv

# Get the Data from the CSV file in the resources folder
Budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open the file using write mode while holding the contents in the correct file
with open(Budget_csv, newline=" ") as csvfile:
csvreader = csv.reader(csvfile, delimiter=",")
print(csvreader)
# Skip the header row
csv_header = next(csvfile)

# Append the values to the correct rows for months and the total profit
for row in csvreader:
total_months.Append(row[0])
total_profit.Append(int(row[1]))

#
