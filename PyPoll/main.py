import os
import csv

# Define all the variables
votes = []
candidates = []
county = []
Khan = []
Correy = []
Li = []
Otooley = []

#Enter path to collect data from the Recources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Open and read the csv file
with open(election_csv, 'r') as csvfile:

    # Split up the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    next(csvreader)
    
    #Loop through the data
    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    for candidate in candidates:
        if candidate == "Khan":
            Khan.append(candidates)
            Khan_votes = len(Khan)
    print(Khan_votes)
    
    
    #Calculate the total number of votes
    total_votes = (len(votes))
    print(total_votes)
    
   
    #Print the results
    print("Khan")
    
