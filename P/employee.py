'''
create a employee class with following private members: empid,empname,basic,hra,da.
  include parameterized constructor and getter-setter property only for basic salary.
    Employee class includes the following public methods:
    showDetail(): shows employee details. computeNetSalary(): take home salary will be calculated after deductions. 
    checkForHike(): computes hike for an employee based on number of projects in hand. 
    The part-time and full-time employees are part of a company and they should be derived from  Employee class. 
     Separate list of part-time and full-time emplyee object will be added to the Company. Create a text file and
      store the employee details those who are getting hike.  Necessary exceptions should be added wherever error is expected.
        Include userdefined exception for hike is morethan 50% of net salary.
'''
class SalaryHikeException(Exception):
    def __init__(self, message="Hike is more than 50% of net salary"):
        self.message = message
        super().__init__(self.message)

class Employee:
    def __init__(self, empid, empname, basic, hra, da):
        self.__empid = empid
        self.__empname = empname
        self.__basic = basic
        self.__hra = hra
        self.__da = da

    def get_basic(self):
        return self.__basic

    def set_basic(self, basic):
        self.__basic = basic

    def show_details(self):
        print(f"Employee ID: {self.__empid}")
        print(f"Employee Name: {self.__empname}")
        print(f"Basic Salary: {self.__basic}")
        print(f"HRA: {self.__hra}")
        print(f"DA: {self.__da}")

    def compute_net_salary(self):
        net_salary = self.__basic + self.__hra + self.__da
        return net_salary

    def check_for_hike(self, projects):
        if projects > 5:
            hike_percentage = 0.1 * projects
            new_salary = self.__basic + (self.__basic * hike_percentage)
            if (new_salary - self.__basic) / self.compute_net_salary() > 0.5:
                raise SalaryHikeException()
            else:
                self.__basic = new_salary
                print(f"Hike granted! New Basic Salary: {self.__basic}")


class PartTimeEmployee(Employee):
    def __init__(self, empid, empname, basic, hra, da, hours_worked, hourly_rate):
        super().__init__(empid, empname, basic, hra, da)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate


class FullTimeEmployee(Employee):
    def __init__(self, empid, empname, basic, hra, da, projects):
        super().__init__(empid, empname, basic, hra, da)
        self.projects = projects


class Company:
    def __init__(self):
        self.part_time_employees = []
        self.full_time_employees = []

    def add_part_time_employee(self, employee):
        self.part_time_employees.append(employee)

    def add_full_time_employee(self, employee):
        self.full_time_employees.append(employee)

    def store_hike_details(self, filename):
        try:
            with open(filename, 'w') as file:
                for employee in self.full_time_employees:
                    try:
                        employee.check_for_hike(employee.projects)
                        file.write(f"{employee.show_details()}\n")
                    except SalaryHikeException as e:
                        print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


# Example usage
company = Company()

part_time_employee = PartTimeEmployee(empid=1, empname="John", basic=5000, hra=1000, da=500, hours_worked=20, hourly_rate=10)
full_time_employee = FullTimeEmployee(empid=2, empname="Jane", basic=8000, hra=1500, da=700, projects=6)

company.add_part_time_employee(part_time_employee)
company.add_full_time_employee(full_time_employee)

company.store_hike_details("hike_details.txt")
