import csv

def read_csv():
    my_data = []
    with open('test.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader, None)
        for row in csv_reader:
            my_data.append(row)
    return my_data
