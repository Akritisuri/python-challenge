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
            Otooley_votes = len(Otooley)
    
    #Calculate the total number of votes
    total_votes = (len(votes))
    
    #Calculate the percentages
    KP = round((Khan_votes / total_votes) * 100, 2)
    CP = round((Correy_votes / total_votes) * 100, 2)
    LP = round((Li_votes / total_votes) * 100, 2)
    OP = round((Otooley_votes / total_votes) * 100, 2)
    
    # To find the winner
    winner = [KP, CP, LP, OP]
    Election_winner = max(winner)

    if Election_winner == KP:
        winner_name = "Khan"
        
    elif Election_winner == CP:
        winner_name = "Correy"
        
    elif Election_winner == LP:
        winner_name = "Li"
        
    else:
        winner_name = "O'Tooley"
        
  
    
    #Print the results
    print("Election Results")
    print("----------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------")
    print(f"Khan: {KP}% ({Khan_votes})")
    print(f"Correy: {CP}% ({Correy_votes})")
    print(f"Li: {LP}% ({Li_votes})")
    print(f"O'Tooley: {OP}% ({Otooley_votes})")
    print("------------------------")
    print(f"Winner: {winner_name}")
    print("-------------------------")

    #Export the output to a text file
    file = open("pypolloutput.txt", "w")
    data = ["Election Results \n",
    "--------------------- \n",
    "Total Votes: {} \n".format(total_votes),
    "--------------------- \n",
    "Khan: {}% ({}) \n".format(KP, Khan_votes),
    "Correy: {}% ({}) \n".format(CP, Correy_votes),
    "Li: {}% ({}) \n".format(LP, Li_votes),
    "O'Tooley: {}% ({}) \n".format(OP, Otooley_votes),
    "--------------------- \n",
    "Winner: {} \n".format(winner_name),
     "--------------------- \n"]
    
    file.writelines(data)
    file.close()

