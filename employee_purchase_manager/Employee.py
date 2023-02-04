#Construct an employee class
#emp id to be auto generated by EmployeeManager class to prevent duplication
#same for discount number. Will be auto generated by Manager
class Employee:
    def __init__(self,name,emp_type,years_worked):
        self.id = 0
        self.name = name
        self.emp_type = emp_type
        self.years_worked = years_worked
        self.emp_disc_num = 0
        self.total_purchased = 0
        self.total_discounts = 0
    
    #individual object print so I can simply loop over the list to print all employees
    def print_employee(self):
        s = self.id, self.name, self.emp_type, self.years_worked, self.total_purchased, self.total_discounts, self.emp_disc_num
        print(s)