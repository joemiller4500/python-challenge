import os
import csv

# Import reference data file - assuming residing in same directory
bank_csv = 'budget_data.csv'

with open(bank_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Initialize variables to proper type after reading as strings
    header = next(csvfile)
    firstStr = next(csvfile)
    firstArr = firstStr.split(",")
    first = int(firstArr[1])
    total = int(first)
    greatInc = int(first)
    greatDec = int(first)
    count = 1

    # Iterate through rows, total changes
    for row in csvreader:
        last = int(row[1])
        total = total + last
        count = count + 1

        # Check for max and min values, populate corresponding variables
        if last > greatInc:
            greatInc = last
            greatIncDate = row[0]
        
        if last < greatDec:
            greatDec = last
            greatDecDate = row[0]

# Calculate final changes
avgChange = int(total / count)
netChange = last - first

# Print results
# print(f"Financial Analysis")
# print(f"-----------------------")
# print(f"Total months: " + str(count))
# print(f"Net change: $" + str(netChange))
# print(f"Average change: $" + str(avgChange))
# print(f"Greatest increase in profits: " + greatIncDate + " ($" + str(greatInc) + ")")
# print(f"Greatest decrease in profits: " + greatDecDate + " ($" + str(greatDec) + ")")

lin1 = "Financial Analysis \n"
lin2 = "------------------------ \n"
lin3 = "Total months: " + str(count) + "\n"
lin4 = "Net change: $" + str(netChange) + "\n"
lin5 = "Average change: $" + str(avgChange) + "\n"
lin6 = "Greatest increase in profits: " + greatIncDate + " ($" + str(greatInc) + ") \n"
lin7 = "Greatest decrease in profits: " + greatDecDate + " ($" + str(greatDec) + ") \n"
L = [lin1,lin2,lin3,lin4,lin5,lin6,lin7]


fileWrite = open("BankResults.txt","w")
fileWrite.writelines(L)
print(lin1)
print(lin2)
print(lin3)
print(lin4)
print(lin5)
print(lin6)
print(lin7)




