# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def __add__(self,num):
        self.i = self.i + num.i
        self.j = self.j + num.j
        return (self.i,self.j)
    
num1=Complex(2,3)
num2=Complex(3,5)

print(num1 +num2)