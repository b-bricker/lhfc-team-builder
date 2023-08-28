import csv

def read_roster(roster_path):
    players = []

    with open(roster_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # next(csv_reader)
        for row in csv_reader:
            del row['Registration Date']
            del row['Order Number']
            del row['Order Status']
            players.append(row)

    return players
