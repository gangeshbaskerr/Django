import csv
import os

# Specify the path where you want to create the CSV file
file_path = 'D:/S5/PYTHON LAB/textttt.csv'

# Data to be written to the CSV file
data = [
    ["Name", "Status", "Income", "FD_List", "Asset_Value_Dict"],
    ["AAA", "Professional", 800000, [1200000, 45000, 300000, 200000], {"House": 4500000, "Car": 600000, "Land": 4000000, "Jewels": 1000000}],
    ["BBB", "Politician", 10000000, [2000000, 1000000, 25000000], {"House": 30000000, "Car": 2000000, "Land": 100000000, "Jewels": 25000000}],
    ["CCC", "Employee", 700000, [500000, 20000000, 150000], {"House": 1000000, "Jewels": 250000}]
]

# Writing to the CSV file
with open(file_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print(f"CSV file created successfully at: {file_path}")
