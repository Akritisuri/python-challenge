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
        elif candidate == "Correy":
            Correy.append(candidates)
            Correy_votes = len(Correy)
        elif candidate == "Li":
            Li.append(candidates)
            Li_votes = len(Li)
        else:
            Otooley.append(candidates)
            Otooley_votes = len(Li)
    print(Khan_votes)
    print(Correy_votes)
    print(Li_votes)
    print(Otooley_votes)
    
    #Calculate the total number of votes
    total_votes = (len(votes))
    print(total_votes)
    
    #Calculate the percentages
    KP = round((Khan_votes / total_votes) * 100, 2)
    CP = round((Correy_votes / total_votes) * 100, 2)
    LP = round((Li_votes / total_votes) * 100, 2)
    OP = round((Otooley_votes / total_votes) * 100, 2)
    
    # To find the winner
    winner = [KP, CP, LP, OP]
    Election_winner = max(winner)
    print(Election_winner)
    if winner == KP:
        winner_name = "Khan"
        
    elif winner == CP:
        winner =
    #Print the results
    print(KP, CP, LP, OP)
    
