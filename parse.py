import csv

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

def main():

    new_data = parse(MY_FILE, ",")

    print(new_data)

if __name__ == "__main__":
    main()