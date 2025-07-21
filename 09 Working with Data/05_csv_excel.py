import csv

from typing import List

data: List[List[str | int]] = [
    ["Name", "Age"],
    ["Mateen", 22],
    ["Ali", 25]
]

with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("people.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
