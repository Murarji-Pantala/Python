#Reading CSV Files 

import csv

with open('Downloads/IPL Sample CSV/Team.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)