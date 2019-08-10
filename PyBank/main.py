import os
import csv

budget_reader = os.path.join("/Users/jorgesanchez/Python-Challenge/PyBank/Resources/budget_data.csv")

with open(budget_reader, newline="") as csvfile:
    # read and split the data on commas and put into string variable budget_reader
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
 
    #confirmed that the csv file is read and is correct by seeing the header

    #create list to store data from functions
    profit = []
    monthly_changes = []
    date = []

    #initialize variables set to zero
    count = 0
    total_profit = 0
    total_change_profits = 0
    initial_profit = 0

# Creating the first output
    for row in csvreader:    
        # Use count to count the number months in this dataset and move through each row
        count = count + 1 
  
        # First row will collect greatest increase and decrease in profits
        date.append(row[0])
  
        # Append the profit information & calculate the total profit through each row, will show at end
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
  
        #Calculate the average change in profits from month to month. Then calulate the average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
  
        #Store these monthly changes in a list
        monthly_changes.append(monthly_change_profits)
  
        total_change_profits = total_change_profits - monthly_change_profits
        initial_profit = final_profit
  
        #Calculate the average change in profits
        average_change_profits = (total_change_profits/count)
        
        #Locate the max and min change in profits and the dates these changes occured
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)
  
        great_increase_date = date[monthly_changes.index(greatest_increase_profits)]
        great_decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
  
        #Create print functions for lay out and output results 

        print("----------------------------------------------------------")
        print("Financial Analysis")
        print("----------------------------------------------------------")
        print("Total Months: " + str(count))
        print("Total Profits: " + "$" + str(total_profit))
        print("Average Change: " + "$" + str(int(average_change_profits)))
        print("Greatest Increase in Profits: " + str(great_increase_date) + " ($" + str(greatest_increase_profits) + ")")
        print("Greatest Decrease in Profits: " + str(great_decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
        print("----------------------------------------------------------")
    
    with open('financial_analysis.txt', 'w') as text:
        text.write("----------------------------------------------------------\n")
        text.write("  Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(count) + "\n")
        text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
        text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(great_increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(great_decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
        text.write("----------------------------------------------------------\n")
