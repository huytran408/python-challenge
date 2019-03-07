import pandas
import csv
import os

file = os.path.join("Resources/election_data.csv")

poll = {}


total_votes = 0
candidates = []
num_votes = []


with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread, None)
    
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

vote_percent = []
for n in num_votes:
    vote_percent.append(round((n/total_votes)*100,2))

clean_data = list(zip(candidates, num_votes, vote_percent))

winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

winner=winner_list[0]

print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
for i in clean_data:
    print(i[0] + ": " + str(i[2]) + "% (" + str(i[1])+ ")")
print("--------------------------")
print("Winner: " + winner)
print("--------------------------")

output = open("Election Results.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = (f"Total Votes: {str(total_votes)}")
line4 = ("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in clean_data:
    line = (i[0] + ": " + str(i[2]) + "% (" + str(i[1])+ ")")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = (f"Winner: {winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

