# import Data
import os

import csv

# ouput
file_to_output = "PyBoss/Analysis/employee_data_reformatted.csv"

# working directory
csvpath = os.path.join('PyBoss', 'Resources', 'employee_data.csv')
# define
emp_ids = []
first_names = []
last_names = []
birth = []
ssns = []
states = []

# read file
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header=next(csvreader)

# state abbreviations defined and stored
    us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
    }
    
    # define
    emp_ids = []
    full_names = []
    first_names = []
    last_names = []
    DOB = []
    birth = []
    ssns = []
    ssn_reformat = []
    states = []

    # Loop through the rows
    for row in csvreader:

        # append emp_id into list
        emp_ids.append(row[0])

        # split names
        full_names = row[1].split(" ")
        first_names.append(full_names[0])
        last_names.append(full_names[1])

        # split DOB and then rearrange
        DOB = row[2].split("-")
        birth.append(DOB[1] + "/" + DOB[2] + "/" + DOB[0])

        # split SSN and reformat
        ssns = row[3].split("-")
        ssn_reformat.append("***-**-" + ssns[2])

        # change state name to abbreviation
        states.append(us_state_abbrev[row[4]])

# put all new lists together
employee_list = zip(emp_ids, first_names, last_names, birth, ssn_reformat, states)

# write to analysis
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # write to textfile
    writer.writerow(["Emp ID", "First Name", "Last Name","DOB", "SSN", "State"])
    writer.writerows(employee_list)