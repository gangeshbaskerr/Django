'''
A university wish to know the progress of the students.
Design a class STUDENT with data member RegNo, Name, E-mail_id, Mobile No.
ACADEMICS that store student details such as, RegNo, Department, and CGPA(CGPA should be validated which is less than or equal to 10.0)
Design a function getDetails (RegisterNumber) in these two classes to obtain the details of a student from the given input register number.
Create another class STUDENT_STATUS that inherit both the classes and call the function getDetails() to display the details and include a function send_email() to send email to the students whose CGPA is less than 5.0
'''
class STUDENT:
    def __init__(self, RegNo, Name, E_mail_id, MobileNo):
        self.RegNo = RegNo
        self.Name = Name
        self.E_mail_id = E_mail_id
        self.MobileNo = MobileNo

    def getDetails(self, RegNo):
        if self.RegNo == RegNo:
            return f"Student Details:\nRegNo: {self.RegNo}\nName: {self.Name}\nE-mail: {self.E_mail_id}\nMobile: {self.MobileNo}"
        else:
            return "Student not found with the given RegNo."

class ACADEMICS(STUDENT):
    def __init__(self, RegNo, Department, CGPA):
        super().__init__(RegNo, "", "", "")  # Call the parent class constructor with empty values for Name, E-mail_id, and MobileNo
        self.Department = Department
        self.setCGPA(CGPA)

    def setCGPA(self, CGPA):
        if 0.0 <= CGPA <= 10.0:
            self.CGPA = CGPA
        else:
            raise ValueError("Invalid CGPA. It should be between 0.0 and 10.0.")

    def getDetails(self, RegNo):
        if self.RegNo == RegNo:
            return f"Student Academic Details:\nRegNo: {self.RegNo}\nDepartment: {self.Department}\nCGPA: {self.CGPA}"
        else:
            return super().getDetails(RegNo)

class STUDENT_STATUS(ACADEMICS):
    def send_email(self):
        if self.CGPA < 5.0:
            print(f"Sending email to {self.Name} ({self.RegNo}) with CGPA {self.CGPA}: Your CGPA is below 5.0. Please improve your academic performance.")

# Example usage
student1 = STUDENT(123, "John Doe", "john.doe@example.com", "1234567890")
academic1 = ACADEMICS(123, "Computer Science", 7.5)
student_status1 = STUDENT_STATUS(123, "Computer Science", 4.2)

print(student1.getDetails(123))
print(academic1.getDetails(123))
print(student_status1.getDetails(123))
student_status1.send_email()
