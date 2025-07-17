# write_csv.py

import csv
from typing import Any

data: list[list[Any]] = [
    ["Name", "Age", "Grade"],
    ["Ahmad", 22, "B"],
    ["Zara", 20, "A+"]
]

with open("new_students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
