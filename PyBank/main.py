import os
import csv

# Get the Data from the CSV file in the resources folder
Budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open the file using write mode while holding the contents in the correct file
with open(Budget_csv, newline=" ") as csvfile:

