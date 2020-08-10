# import Data
import os

import csv

# working directory
csvpath = os.path.join('Resources', 'election_data.csv')

# read file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    header=next(csvreader)
   
 #define  
    voter_id = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    # votes, county, & candidates
    for row in csvfile:
        voter_id.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])
    
    # total vote
    total_votes = len(voter_id)
    print(total_votes)

    # voter per person
    for candidate in candidates:
        if candidate == "Kahn":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.appen(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
    print(khan_votes)
    print(correy_votes)
    print(li_votes)
    print(otooley_votes)
