# 5. Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self,v):
        self.v=v
    def __add__(self,vec):
        return ([self.v[0] + vec.v[0],self.v[1] + vec.v[1],self.v[2] + vec.v[2]])
    def __mul__(self,vec):
        return ((self.v[0] * vec.v[0]) + (self.v[1] * vec.v[1]) +(self.v[2] * vec.v[2]))

v1=Vector([1,4,5])
v2=Vector([2,2,2])
print(v1+v2,v1*v2)
