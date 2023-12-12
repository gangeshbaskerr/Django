''' Write a python program that asks the students to enter Name,
Reg. No, Gender, Date of Birth, ID Verified (such as Aadhaar/PAN),
Vaccine Name, Date of First Dose, and Date of Second Dose for N students.
Also store them in a list named as Vaccination_details.'''

from datetime import datetime, timedelta

def calculate_age(dob):
    today = datetime.today()
    birth_date = datetime.strptime(dob, "%d.%m.%Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def calculate_next_due_date(date_first_dose):
    date_first_dose = datetime.strptime(date_first_dose, "%d.%m.%Y")
    next_due_date = date_first_dose + timedelta(days=84)  # Assuming an 84-day gap for Covishield
    return next_due_date.strftime("%d.%m.%Y")

def vaccination_status(date_second_dose):
    if date_second_dose == "NA":
        return "Not Applicable"
    else:
        return "Fully vaccinated"

def generate_email(reg_no):
    return f"{reg_no}@sastra.ac.in"

def main():
    try:
        num_students = int(input("Enter the number of students: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    vaccination_details = []

    for _ in range(num_students):
        print(f"\nEnter details for Student {_ + 1}:")
        name = input("Enter Name: ")
        reg_no = input("Enter Reg. No.: ")
        gender = input("Enter Gender: ")
        dob = input("Enter Date of Birth (DD.MM.YYYY): ")
        id_verified = input("Enter ID Verified (Aadhaar/PAN): ")
        vaccine_name = input("Enter Vaccine Name: ")
        date_first_dose = input("Enter Date of First Dose (DD.MM.YYYY): ")
        date_second_dose = input("Enter Date of Second Dose (DD.MM.YYYY) or 'NA' if not applicable: ")

        age = calculate_age(dob)
        email = generate_email(reg_no)
        next_due_date = calculate_next_due_date(date_first_dose)
        status = vaccination_status(date_second_dose)

        student_details = {
            "Name": name,
            "Reg. No": reg_no,
            "Email": email,
            "Gender": gender,
            "DOB": dob,
            "Age": age,
            "ID Verified": id_verified,
            "Vaccine Name": vaccine_name,
            "Date of First Dose": date_first_dose,
            "Next Due Date": next_due_date,
            "Date of Second Dose": date_second_dose,
            "Vaccination Status": status,
        }

        vaccination_details.append(student_details)

    print("\nVaccination Details:")
    print("\nName Reg. No. Email Gender DOB Age ID Verified Vaccine Name Date of 1 Dose Next Due Date Date of 2 Dose Vaccination Status")
    for details in vaccination_details:
        print(f"{details['Name']} {details['Reg. No']} {details['Email']} {details['Gender']} {details['DOB']} {details['Age']} {details['ID Verified']} {details['Vaccine Name']} {details['Date of First Dose']} {details['Next Due Date']} {details['Date of Second Dose']} {details['Vaccination Status']}")

if __name__ == "__main__":
    main()
