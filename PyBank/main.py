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
    revenue_change = []

    # month and revenue      
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    print(len(month))

    #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print("$" + str(total_revenue))

     #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        revenue_loss = int(revenue[i+1]) - int(revenue[i])

    # append profit_loss
        revenue_change.append(revenue_loss)
    Total = sum(revenue_change)

    # print(revenue_change)
    monthly_change = Total / len(revenue_change)
    print("$" + str(monthly_change))
  
    # greatest increase value
    revenue_increase = max(revenue_change)
    print("$" + str(revenue_increase))

    # greatest increase month
    x = revenue_change.index(revenue_increase)
    month_increase = month[x+1]
    print(month_increase)

    # greatest decrease value
    revenue_decrease = min(revenue_change)
    print("$" + str(revenue_decrease))

    # greatest decrease month
    z = revenue_change.index(revenue_decrease)
    month_decrease = month[z+1]
    print(month_decrease)
