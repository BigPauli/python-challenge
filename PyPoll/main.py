# initialize counter dictionary that will contain votes
counter = {}

# use with-open syntax to open the data csv
with open("Resources/election_data.csv", "r") as data:
    # load in the data as a list of lines
    lines = data.readlines()

    # the total number of votes will be the length of lines minus the header
    total_votes = len(lines) - 1

    # save the header
    header = lines[0]

    # iterate over every line in the data
    for i in lines[1:]:

        # use tuple unpacking to extract the candidate that was voted for. Remove new line character at the end of candidate's name using strip()
        _, _, candidate = i.split(",")
        candidate = candidate.strip()

        # increment the counter for the candidate by 1. Using the get() function with a default value of 0 to prevent errors where the candidate is not yet in the dictionary
        counter[candidate] = counter.get(candidate, 0) + 1

# creating the analysis as a multi-line f-string

analysis = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# programatically add all of the candidates with their number of votes to the end of the analysis using a for loop over the keys and values in the counter dictionary
for key, val in counter.items():
    analysis += f"{key}: {round((val/total_votes)*100,3)}% ({val})\n"


# create list of all competitors sorted by the amount of votes they have in descending order. Therefore the first element in the list will be the winner
competitors = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)

# add winner to analysis string
analysis += f"""-------------------------
Winner: {competitors[0]}
-------------------------
"""

# write analysis string to analysis.txt located in the analysis folder within the same directory
with open("analysis/analysis.txt", "w") as file:
    file.write(analysis)

print(analysis)