import csv

with open('age.csv') as f:
    data = csv.reader(f)
    for row in data:
        print(row)