# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        print("Squre is",self.num**2)
    def cube(self):
        print("Cube is",self.num**3)
    def squareroot(self):
        print("Squreroot is",self.num**0.5)

num1 = Calculator(4)
num1.cube()
num1.square()
num1.squareroot()