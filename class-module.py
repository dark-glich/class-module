
class employe:
    def __init__(self, name, age, salary, working_days):
        self.name = name
        self.age = age
        self.salary = salary
        self.working_days = working_days

employee_1 = employe("irfan", 22, 6500, "6")
employee_2 = employe("javed", 38, 7200, "6")
employee_3 = employe("naseem", 28, 8500, "7")
employee_4 = employe("shoeb", 26, 7900, "5")
employee_5 = employe("naved", 42, 8500, "5")

print(" _______________________________________________________________")
print("|               |          |               |                    |")
print(f"| name : {employee_1.name}  | age : {employee_1.age} | salary : {employee_1.salary} | working days : {employee_1.working_days}   |".upper())
print(f"| name : {employee_2.name}  | age : {employee_2.age} | salary : {employee_2.salary} | working days : {employee_2.working_days}   |".upper())
print(f"| name : {employee_3.name} | age : {employee_3.age} | salary : {employee_3.salary} | working days : {employee_3.working_days}   |".upper())
print(f"| name : {employee_4.name}  | age : {employee_4.age} | salary : {employee_4.salary} | working days : {employee_4.working_days}   |".upper())
print(f"| name : {employee_5.name}  | age : {employee_5.age} | salary : {employee_5.salary} | working days : {employee_5.working_days}   |".upper())
print("|_______________|__________|_______________|____________________|")

class total(employe):
    def __init__(self, name, age, salary, working_days):
        super().__init__(name,age, salary, working_days)
    
    @staticmethod
    def from_max (a, b, c, d, e):
        p = [a, b, c, d, e]
        return max(p)
        
    @staticmethod
    def sum_salary (a, b, c, d, e):
        summ = a + b + c + d + e
        return summ

total_emp = 5
total_salary = total.sum_salary(employee_1.salary, employee_2.salary, employee_3.salary, employee_4.salary, employee_5.salary)

max_working_days = total.from_max(employee_1.working_days, employee_2.working_days, employee_3.working_days, employee_4.working_days, employee_5.working_days)

max_employee_age = total.from_max(employee_1.age, employee_2.age, employee_3.age, employee_4.age, employee_5.age)

state = total(total_emp, max_employee_age, total_salary, max_working_days)

print(" __________________________________\n|                      |           |")
print(f"|   Total Employees :  |  : {state.name}      |".upper())
print(f"|   Maximum Age     :  |  : {state.age} Yrs |".upper())
print(f"|   Total Salary    :  |  : ₹{state.salary} |".upper())
print(f"|   Max Working Days:  |  : {state.working_days} Days |".upper())
print("|______________________|___________|")


        

