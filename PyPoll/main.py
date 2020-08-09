# import Data
import os

import csv

# working directory
csvpath = os.path.join('Resources', 'election_data.csv')

# read file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)
    voter_id = []
    county = []
    candidate = []

