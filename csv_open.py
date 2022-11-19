import csv

with open("data2.csv")as r_file:
    file_rider = csv.reader(r_file, delimiter=";")
    for row in file_rider:
        print(row)


























