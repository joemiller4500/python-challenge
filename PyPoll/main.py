import os
import csv

# Import reference data file from same directory as this code
poll_csv = 'election_data.csv'

# Load file for reading
with open(poll_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvfile)
    candListArr = {}
    # Iterate through rows to collect results
    for row in csvreader:
        if not row[2] in candListArr:
            candListArr[row[2]] = 1
        if row[2] in candListArr:
            candListArr[row[2]] += 1
        else:
            print("no")

# Initialize variables for indexing results
winIndex = 0
total = 0

# Take total votes
for i in candListArr:
    total = total + candListArr[i]

# Find winner
for i in candListArr:
    if candListArr[i] > winIndex:
        winner = i

# Populate array for printing and exporting results
lin = [
    "Election Resuluts\n",
    "-------------------------\n"
    ]

for i in candListArr:
    tempPerc = candListArr[i] / total
    tempStr = str(i) + ": " + str('{:.1%}'.format(tempPerc)) + " (" + str(candListArr[i]) + ")\n"
    lin.append(tempStr)

# Write to external file
fileWrite = open("ElectionResults.txt","w")
for item in lin:
    fileWrite.writelines(item)

# Print results
for item in lin:
    print(item)
