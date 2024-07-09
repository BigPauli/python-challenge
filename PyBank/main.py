# initialize total_change
total_change = 0

#initialize tuples that contain the greatest increase and greatest decrease months/values
greatest_increase = (None, -float("inf"))
greatest_decrease = (None, float("inf"))

# use with-open syntax to open file
with open("Resources/budget_data.csv", "r") as data:

    lines = data.readlines()
    months = len(lines)-1

    # store header row
    header = lines[0].split(",")
    header[1] = header[1][:-1]

    # initialize profit and total from first month
    prev = int(lines[1].split(",")[1])
    total = prev
    # iterate over every line in the data, starting at idx 1
    for idx in range(2, len(lines)):

        # extract data from line using tuple unpacking and convert
        curr_month, money = lines[idx].split(",")
        money = int(money)

        # calculate profit change from previous month
        change = money - prev

        # add to totals
        total += money
        total_change += change

        # update greatest increase and greatest decrease, if necessary
        if change > greatest_increase[1]:
            greatest_increase = (curr_month, change)
        if change < greatest_decrease[1]:
            greatest_decrease = (curr_month, change)

        # update prev
        prev = money

# create analysis and print it
analysis = f"""
Financial Analysis
----------------------------
Total Months: {months}
Total: ${total}
Average Change: ${round(total_change/(months-1), 2)}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

print(analysis)

# write analysis to file. Code written with assistance from https://www.w3schools.com/python/python_file_write.asp
with open("analysis/analysis.txt", "w") as file:
    file.write(analysis)