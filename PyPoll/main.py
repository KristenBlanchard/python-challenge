# import Data
import os

import csv

# working directory
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# read file
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
   
    header = next(csvreader)
   
 #define  
    voter = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    # votes, county, & candidates
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
    
    # total vote
    total_votes = len(voter)


    # votes per person
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidate)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidate)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidate)
            li_votes = len(li)
        else:
            otooley.append(candidate)
            otooley_votes = len(otooley)

# percentage per person
    khan_percent = round(((khan_votes / total_votes)* 100),2)
    correy_percent = round(((correy_votes / total_votes)* 100),2)
    li_percent = round(((li_votes / total_votes)* 100),2)
    otooley_percent = round(((otooley_votes / total_votes)* 100),2)

# Determining the winner
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"
    elif li_percent > max(khan_percent, correy_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

# print final statements
print(f"Election Results")
print(f"-----------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------------")
print(f"Khan: {khan_percent}% ({khan_votes})")
print(f"Correy: {correy_percent}% ({correy_votes})")
print(f"Li: {li_percent}% ({li_votes})")
print(f"O'Tooley: {otooley_percent}% ({otooley_votes})")
print(f"-----------------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------------")

# output all the data

# write to analysis
output_file = os.path.join('PyPoll', 'Analysis', 'poll_results.txt')

with open(output_file, 'w',) as txtfile:
    
    # write to poll results
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-----------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"-----------------------------------\n")
    txtfile.write(f"Khan: {khan_percent}% ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent}% ({correy_votes})\n")
    txtfile.write(f"Li: {li_percent}% ({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})\n")
    txtfile.write(f"-----------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"-----------------------------------")