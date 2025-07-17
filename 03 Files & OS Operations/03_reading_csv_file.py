# read_csv.py

import csv

with open("new_students.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("new_students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(
            f"{row['Name']} is {row['Age']} years old and got grade {row['Grade']}")
