# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self,num):
        self.num=num

    def greet(self):
        print("Hello ! User")
    def square(self):
        print("Squre is",self.num**2)
    def cube(self):
        print("Cube is",self.num**3)
    def squareroot(self):
        print("Squreroot is",self.num**0.5)

num1 = Calculator(4)
num1.greet()
num1.cube()
num1.square()
num1.squareroot()