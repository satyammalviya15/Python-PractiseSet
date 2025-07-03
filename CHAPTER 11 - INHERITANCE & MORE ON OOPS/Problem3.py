# 3. Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    def add_salary(self,value):
        self.salary=value
        self.increment=1.0

    @property
    def salaryAfterIncrement(self):
        return (self.salary*self.increment)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.new_salary=salary
        self.increment = (self.new_salary/self.salary)


Employee1 = Employee()
Employee1.add_salary(70000)
Employee1.salaryAfterIncrement = 140000
print(Employee1.salaryAfterIncrement)
