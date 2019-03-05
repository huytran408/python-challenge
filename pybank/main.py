import os
import csv

csv_path = os.path.join("budget_data.csv")

total_months = 0
months = []
revenue = []


with open(csv_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    next(csvreader)

    for row in csvreader:
    	months.append(row[0])
    	revenue.append(int(row[1]))

total_months=len(months)

greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0
for r in range(len(revenue)):
	if revenue[r] >= greatest_inc:
		greatest_inc = revenue[r]
		greatest_inc_month = months[r]
	elif revenue[r] <= greatest_dec:
		greatest_dec = revenue[r]
		greatest_dec_month = months[r]
	total_revenue+=revenue[r]

average_change= round(total_revenue/total_months,2)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_revenue)}")
print(f"Average Change: ${str(average_change)}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${str(greatest_inc)})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${str(greatest_dec)})")

output = open("Budget analysis output.txt","w")

line1 = str("Financial Analysis")
line2 = str("---------------------")
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_revenue)}")
line5 = str(f"Average Change: ${str(average_change)}")
line6 = str(f"Greatest Increase in Profits: {greatest_inc_month} (${str(greatest_inc)})")
line7 = str(f"Greatest Decrease in Profits: {greatest_dec_month} (${str(greatest_dec)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))