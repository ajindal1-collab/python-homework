from pathlib import Path
import csv

# Set the file path
csvpath = Path('../Pybank/budget_data.csv')

with open(csvpath, 'r') as csvfile:
     
    # Pass in the csv file to the csv.Dictreader() function
    
    csvreader = csv.reader(csvfile, delimiter=',')
   
   
   #Print the months out
#     for row in csvreader:
#         print(row['Date'])

#     #Print the sum of months
#     lines= len(list(csvreader))
#     print(lines)
    
    #Net Total amount of profit/losses over entire period
    positive = 0
    Loss = 0
    for row in csvreader:
        amount = (row["Profit/Losses"])
        if row < 0:
            print(sum(loss))
       
    

        
        
# Establish variables
toal = 0
Profit = 0
loss = 0
increase = 0
month = 0

    
        