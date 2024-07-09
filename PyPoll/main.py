counter = 0

with open("Resources/election_data.csv", "r") as data:
    for i in data.readlines():
        counter += 1
        print(i)