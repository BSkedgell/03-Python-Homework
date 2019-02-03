# Modules
import os
import csv

# Set input path for the csv file
csvpath = os.path.join('Resources', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

# Open the file in "read" mode ('r') 
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Returns next item from csvreader
    next(csvreader)

    #Define your variables
    total_sum = 0
    row_count = 0
    total_var = 0
    top_total_change = 0
    low_total_change = 0
    total_var_overall = 0
    current_total = 0
    last_total = 0



    #Start the for loop for each row in the csvreader
    for row in csvreader:

        #Row count defines first variable as row_count and set value for each row in csvpath
        row_count = row_count+1
        total_sum = float(total_sum)+float(row[1])
        current_total = row[1]
        total_var = float(current_total)-float(last_total)
        total_var_overall = total_var_overall+total_var
        last_total = row[1]


        if total_var > top_total_change:
            top_total_change = total_var
            top_total_month= row[0]
        if total_var < low_total_change:
            low_total_change = total_var
            low_total_month= row[0]
            
    avg_total_var = total_var_overall/row_count

#print all of you results 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${round(total_sum)}")
print(f"Average Total Change: ${round(avg_total_var,2)}")
print(f"Greatest Increase in Profits: {top_total_month} ${round(top_total_change)}")
print(f"Greatest Decrease in Profits: {low_total_month} ${round(low_total_change)}")




