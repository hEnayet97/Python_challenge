# -*- coding: UTF-8 -*-

# Import necessary modules
import csv
import os

# Input file path
election_csv = "PyPoll\\Resources\\election_data.csv"

# Track the total number of votes cast
total_votes = 0  

# Define lists and dictionaries to track candidate names and vote counts
Candidate_Name = []
Vote_count = {}
Vote_percent = {}

# Winning Candidate and Winning Count Tracker
Winner = ""
Winner_count = 0

# Open the CSV file and process it
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csv_reader)

    # Loop through each row of the dataset and process it
    for row in csv_reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        Name = row[2]

        # If the candidate is not already in the candidate list, add them
        if Name not in Candidate_Name:
            Candidate_Name.append(Name)
            Vote_count[Name] = 0
        Vote_count[Name] += 1 

# Print the total vote count (to terminal)
print(f'Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------')


file_to_output = "PyPoll\\Analysis\\election_analysis.txt"
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Write the total vote count to the text file
    txt_file.write(f'Election Results\n')
    txt_file.write('----------------------------\n')
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write('----------------------------\n')

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in Vote_count:
        # Get the vote count and calculate the percentage
        votes = Vote_count[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > Winner_count:
            Winner_count = votes
            Winner = candidate

        # Print and save each candidate's vote count and percentage
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)

    # Generate and print the winning candidate summary
    winner_summary = f'Winner: {Winner}\n'
    print(winner_summary)
    txt_file.write('----------------------------\n')
    txt_file.write(winner_summary)
    txt_file.write('----------------------------\n')
