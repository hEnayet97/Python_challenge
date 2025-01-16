# -*- coding: UTF-8 -*-

# Dependencies
import csv

# Input file path
budget_csv = "PyBank\\Resources\\budget_data.csv" 

# Define variables to track the financial data
total_months = 0
total_profit_loss = 0
previous_net = 0
current_net = 0

# Add more variables to track other necessary financial data
net_change_list = []
month_of_change = []

# Open and read the csv
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csv_reader)

    # Track the total and net change
    for row in csv_reader:
        # Track the total months
        total_months += 1

        # Track total profit/loss
        current_net = int(row[1])
        total_profit_loss += current_net
        
        # Track the net change in Profit/loss
        if total_months == 1:
            previous_net = current_net
        else:
            net_profit_loss = current_net - previous_net
            net_change_list.append(net_profit_loss)
            month_of_change.append(row[0])

        # Reset the current and previous months for the next iteration
        previous_net = current_net

# Calculate total change "Profit/Losses" over the entire period
sum_profit_loss = sum(net_change_list)

# Calculate the average net change across the months
average_profit_loss = round(sum_profit_loss / len(net_change_list), 2)

# Calculate the greatest increase in profits (month and amount)
greatest_change = max(net_change_list)
greatest_month = month_of_change[net_change_list.index(greatest_change)]

# Calculate the greatest decrease in losses (month and amount)
lowest_change = min(net_change_list)
lowest_month = month_of_change[net_change_list.index(lowest_change)]

# Print the output summary
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total Profits: " + "$" + str(total_profit_loss))
print("Average Change: " + "$" + str(average_profit_loss))
print("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_change) + ")")
print("Greatest Decrease in Profits: " + lowest_month + " ($" + str(lowest_change) + ")")

# Output file path
output = "PyBank\\Analysis\\budget_analysis.txt"

# Write the results to a text file
with open(output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Total Months: " + str(total_months) + "\n")
    txt_file.write("Total Profits: " + "$" + str(total_profit_loss) + "\n")
    txt_file.write("Average Change: " + "$" + str(average_profit_loss) + "\n")
    txt_file.write("Greatest Increase in Profits: " + greatest_month + " ($" + str(greatest_change) + ")\n")
    txt_file.write("Greatest Decrease in Profits: " + lowest_month + " ($" + str(lowest_change) + ")\n")