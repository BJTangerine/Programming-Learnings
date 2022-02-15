# Inheritance exercise using employee/manager classes with method inheritance.

class Employee:
    def __init__(self, name, salary=30000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

        
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    # contructor accepts several parameters, call the constructor of Employee class with name/salary parameters
    # and creates a project attribute.
    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # method that accepts the same parameters as Employee.give_raise(), plus a bonus parameter with the default value of 1.05 (bonus of 5%),
    # multiples amount by bonus, and uses Employee's method to raise salary by that product.
    def give_raise(self, amount, bonus=1.05):
        return Employee.give_raise(self, (amount * bonus))
    
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(1000)
print(mngr.salary)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)