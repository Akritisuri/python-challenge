import os
import csv

# Get the Data from the CSV file in the resources folder
Budget_csv = os.path.join("Resources", "budget_data.csv")

# Open the file using the read function
with open(Budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    # Skip the header row
    print(f"Header: {csv_header}")

    # Append the values to the correct rows for months and the total profit
    months = []
    profit = []
    
    # Loop through the data
    for row in csvreader:
       profit.append(int(row[1]))
       months.append(row[0])

    # Find the change in revenue
    revenue_change = []

    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))
    
    # Calculate the average
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    #Calculate the greatest increase in profits over the entire period
    greatest_increase = max(revenue_change)
    # Calculate the greatest decrease in profits over the entire period
    greatest_decrease = min(revenue_change)

    # Print the analysis
    print("Financial Analysis")
    
    print("----------------------------------")
    
    print("Total months: ", len(months))
    
    print("Total: " + "$" + str(sum(profit)))
    
    print("Average change: " + "$" + str(revenue_average))
    
    print("Greatest increase in profits: {} (${})".format(str(months[revenue_change.index(max(revenue_change))+1]), str(greatest_increase)))
    
    print("Greatest decrease in profits: {} (${})".format(str(months[revenue_change.index(min(revenue_change))+1]), str(greatest_decrease)))
    
    # Export the output to a text file
    file = open("pybankoutput.txt", "w")
    data = ["Financial Analysis \n", "------------------------- \n", "Total Months: {} \n".format(len(months)), "Total: ${} \n".format(str(revenue_average)), "Greatest increase in profits: {} (${}) \n".format(str(months[revenue_change.index(max(revenue_change))+1]), str(greatest_increase)), "Greatest decrease in profits: {} (${})".format(str(months[revenue_change.index(min(revenue_change))+1]), str(greatest_decrease))]

    file.writelines(data)
    file.close()
