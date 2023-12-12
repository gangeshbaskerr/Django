
from django.shortcuts import render
import csv

def home(request):
    return render(request,"home.html")

def createCand_List(file_path):
    candidate_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['Name']
            status = row['Status']
            income = int(row['Income'])
            fd_list = [int(x) for x in row['FD_List'].strip('[]').split(',')]
            asset_value_dict = eval(row['Asset_Value_Dict'])  # Convert string representation to dictionary
            person = Person(name, status, income, fd_list, asset_value_dict)
            candidate_list.append(person)
    return candidate_list

class Person:
    def __init__(self, name, status, income, fd_list, asset_value_dict):
        self.name = name
        self.status = status
        self.income = income
        self.total_deposits = sum(fd_list)
        self.total_assets = sum(asset_value_dict.values())

    def check_candidature(self):
        if (
            (self.status == 'Professional' and (self.total_deposits > 10 * self.income or self.total_assets > 25 * self.income))
            or (self.status == 'Politician' and (self.total_deposits > 10 * self.income and self.total_assets > 10 * self.income))
            or (self.status == 'Employee' and (self.total_deposits > 20 * self.income or self.total_assets > 20 * self.income))
        ):
            raise ValueError("IT Raid Alert" if self.status == 'Professional' else "Disproportionate Assets Alert" if self.status == 'Politician' else "Scam Alert")

    def __str__(self):
        return f"{self.name}, {self.status}, {self.income}, {self.total_deposits}, {self.total_assets}"


def mcandidate(request):
    file_path = "D:/S5/PYTHON LAB/textttt.csv"
    candidate_list = createCand_List(file_path)
    messages = []

    for c in candidate_list:  # Change the loop variable name
        try:
            c.check_candidature()
            messages.append(f"Good: {str(c)}")
        except ValueError as e:
            messages.append(f"Alert: {e}")

    return render(request, 'mcandidate.html', {'messages': messages})