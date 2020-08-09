# import Data
import os

import csv

# working directory
csvpath = os.path.join('Resources', 'budget_data.csv')

# read file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)
    month = []
    revenue = []

    # month and revenue      
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))