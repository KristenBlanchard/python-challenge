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
    
    #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))

     #Avg Change
    i = 0
    for i in range(len(revenue) - 1):
        revenue_loss = int(revenue[i+1]) - int(revenue[i])

    # append profit_loss
        revenue_change.append(revenue_loss)
    Total = sum(revenue_change)

    # print(revenue_change)
    monthly_change = Total / len(revenue_change)
  
    # greatest increase value
    revenue_increase = max(revenue_change)

    # greatest increase month
    x = revenue_change.index(revenue_increase)
    month_increase = month[x+1]

    # greatest decrease value
    revenue_decrease = min(revenue_change)

    # greatest decrease month
    z = revenue_change.index(revenue_decrease)
    month_decrease = month[z+1]

# final Print Statements

# print title
print('Financial Analysis')
print('----------------------------')

# Print final wanted informtation - propper formatting
print("Total Months: " + str(len(month)))
print("Total: $ " + str(total_revenue))
print("Average Change: $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${revenue_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${revenue_decrease})")

# output all the data

# write to analysis
output_file = os.path.join('..', 'PyBank', 'Analysis', 'Bank_results.txt')

with open(output_file, 'w') as txtfile:
    
    # write to poll results
    txtfile.write('Financial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write("Total Months: " + str(len(month))+'\n')
    txtfile.write("Total: $ " + str(total_revenue)+'\n')
    txtfile.write("Average Change: $" + str(monthly_change)+'\n')
    txtfile.write(f"Greatest Increase in Profits: {month_increase} (${revenue_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {month_decrease} (${revenue_decrease})")