'''
Write a python code to implement the system to maintain an apartment data. An apartment have Ground floor for parking and 3 floors contains 10 houses each (totally 30 houses). Create a module named "APARTMENT" to finish the objectives from a to d.
a) House numbers starts for FIRST floor: F1 to F10, SECOND floor: $1 to $10 and THIRD floor: T1 to T10. GROUND floor parking slot number starts from P1 to P30.
Create separate tuple for each floor with the name as follows: FIRST, SECOND, THIRD and GROUND and house numbers as their data.
Example: FIRST = ("F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10")
b) Create Separate List for House Owners which contains the name of house owners as their data (As String). The Lists name must be as follows: FIRST_OWNERS, SECOND_OWNERS, and THIRD OWNERS.
c) Create a list "House_Numbers" which contains all the house numbers of all the floors by joining all the house numbers) and "OWNERS" list which contains all the house owners name ordered from FIRST floor to THIRD floor. Create a dictionary named "PROPERTY" which contains keys from "House_Numbers" and values from "OWNERS"
Example:
House_Numbers = ["F1", ..... "F10", "S1",...., "S10", "T1",...," "T10"]
OWNERS = ["NAME1", "NAME2",
,"NAME30"]
PROPERTY = { "F1" : "NAME1", “S1” : “NAME11”, "T1" "NAME21", "10": "NAME30"}
d) Create a function "PARKING" which creates a dictionary named "PARKING SLOT" which contains keys from "House_Numbers" list and values from the set "Parking_Number"
'''
class APARTMENT:
    def __init__(self):
        self.FIRST = tuple(f"F{i}" for i in range(1, 11))
        self.SECOND = tuple(f"S{i}" for i in range(1, 11))
        self.THIRD = tuple(f"T{i}" for i in range(1, 11))
        self.GROUND = tuple(f"P{i}" for i in range(1, 31))

        self.FIRST_OWNERS = []
        self.SECOND_OWNERS = []
        self.THIRD_OWNERS = []

        self.House_Numbers = list(self.FIRST + self.SECOND + self.THIRD)
        self.OWNERS = []

        self.PROPERTY = {}
        self.PARKING_SLOT = {}

    def PARKING(self):
        parking_numbers = set(range(1, 31))
        self.PARKING_SLOT = {house_number: parking_numbers.pop() for house_number in self.House_Numbers}

    def EDIT_OWNER(self, house_number, new_owner):
        if house_number in self.PROPERTY:
            current_owner = self.PROPERTY[house_number]
            index = self.OWNERS.index(current_owner)

            if house_number.startswith('F'):
                self.FIRST_OWNERS[index] = new_owner
            elif house_number.startswith('S'):
                self.SECOND_OWNERS[index] = new_owner
            elif house_number.startswith('T'):
                self.THIRD_OWNERS[index] = new_owner

            self.PROPERTY[house_number] = new_owner

    def search_owner(self, house_number):
        if house_number in self.PROPERTY:
            owner = self.PROPERTY[house_number]
            parking_slot = self.PARKING_SLOT[house_number]
            print(f"House Owner Name: {owner}\nParking Slot Number: {parking_slot}")
        else:
            print(f"No owner found for house number {house_number}")

# Example Usage:
apartment = APARTMENT()

# Assigning owners to houses
apartment.FIRST_OWNERS = ["Owner1", "Owner2", "Owner3", "Owner4", "Owner5", "Owner6", "Owner7", "Owner8", "Owner9", "Owner10"]
apartment.SECOND_OWNERS = ["Owner11", "Owner12", "Owner13", "Owner14", "Owner15", "Owner16", "Owner17", "Owner18", "Owner19", "Owner20"]
apartment.THIRD_OWNERS = ["Owner21", "Owner22", "Owner23", "Owner24", "Owner25", "Owner26", "Owner27", "Owner28", "Owner29", "Owner30"]

apartment.OWNERS = apartment.FIRST_OWNERS + apartment.SECOND_OWNERS + apartment.THIRD_OWNERS

# Creating PROPERTY dictionary
apartment.PROPERTY = dict(zip(apartment.House_Numbers, apartment.OWNERS))

# Creating PARKING_SLOT dictionary
apartment.PARKING()

# Editing owner details
apartment.EDIT_OWNER("F2", "NewOwner3")

# Searching for owner by house number
apartment.search_owner("F2")
