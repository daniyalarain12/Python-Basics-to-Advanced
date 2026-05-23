# DEFINE AN Employee class WITH ATTRIBUTES role, department and salary. THIS class ALSO HAS A showDetails() METHOD.
# CREATE AN Engineer class THAT INHERITS PROPERTIES FROM Employee AND HAS ADDITIONAL ATTRIBUTES name and age.

class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.dept = dept
        self.sal = sal
    def showDetails(self):
        print("ROLE :",self.role)
        print("DEPARTMENT :",self.dept)
        print("SALARY :",self.sal)
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("ENGINEER","IT","800000")

emp1 = Employee("ACCOUNTANT","FINANCE",500000)
emp1.showDetails()

eng2 = Engineer("DANIYAL",20)
eng2.showDetails()
