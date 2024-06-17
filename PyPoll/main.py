import os
import csv


# Define the path to the CSV file
file_path = '/Users/ellengrant/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv'
output_path = 'election_results.txt'

# Initialize a dictionary to store candidate votes
candidate_votes = {}

# Read the CSV file
with open(file_path, mode='r', newline='') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the total number of votes
total_votes = sum(candidate_votes.values())

# Prepare the results
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
results.append("-------------------------")
winner = max(candidate_votes, key=candidate_votes.get)
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Print the results to the terminal
for line in results:
    print(line)

# Export the results to a text file
with open(output_path, mode='w') as file:
    for line in results:
        file.write(line + "\n")

print(f"\nResults have been exported to {output_path}")