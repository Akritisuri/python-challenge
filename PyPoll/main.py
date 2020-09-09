import os
import csv

# Define all the variables
total_votes = 0
candidates = []
votes_won = [0, 0, 0, 0]
percent_won = []

#Enter path to collect data from the Recources folder
election_csv = os.path.join("Python-challenge\Resources", 'election_data.csv')
