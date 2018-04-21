from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""

    # Open CSV file
    opened_file = open(raw_file, 'r')

    # Read CSV file
    csv_data = csv.reader(opened_file, delimiter=delimiter)

    # Build a data structure to return parsed_data

    # Setup empty list
    parsed_data = []

    # Skip the first row of the file for headers
    fields = next(csv_data)

    # Iterate over each row of the csv file
    for row in csv_data:

        # Combine the column headers with values in a dictionary and add to list
        parsed_data.append(dict(zip(fields, row)))

    # Close CSV file
    opened_file.close()

    return parsed_data

def visualize_days():
    """Visualize data by day of week"""

    # Grab data that was parsed earlier
    data_file = parse(MY_FILE, ",")

    # Make a new variable 'counter' from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate the x-axis data (the days of the week) from
    # the 'counter' variable variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
                counter["Monday"],
                counter["Tuesday"],
                counter["Wednesday"],
                counter["Thursday"],
                counter["Friday"],
                counter["Saturday"],
                counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thur", "Fri", "Sat", "Sun"])

    # Assign y-axis data to a matplotlib plot instance
    plt.plot(data_list)

    # Create ticks on the x-axis and assign labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the plot
    plt.savefig("Days.png")

    # Close the plot file
    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph"""

    # Grab parsed data
    data_file = parse(MY_FILE, ",")

    # Make a new dictionary variable 'counter' by iterating each line in parsed
    # data and count number of incidents by category
    counter = Counter(item["Category"] for item in data_file)

    # Set labels based on the keys of the counter
    labels = tuple(counter.keys())

    # Set where labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar that will be plotted
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give more room for x-axis labels
    plt.subplots_adjust(bottom=0.4)

    # Make overall graph larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph
    plt.savefig("Type.png")

    # Close the graph
    plt.clf

def main():
    # visualize_days()
    visualize_type()

if __name__ == "__main__":
    main()
