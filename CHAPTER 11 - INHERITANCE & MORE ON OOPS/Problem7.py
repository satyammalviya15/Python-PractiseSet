# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self,v):
        self.v=v
    def __add__(self,vec):
        return ([self.v[0] + vec.v[0],self.v[1] + vec.v[1],self.v[2] + vec.v[2]])
    def __mul__(self,vec):
        return ((self.v[0] * vec.v[0]) + (self.v[1] * vec.v[1]) +(self.v[2] * vec.v[2]))
    def __len__(self):
        return len(self.v)

v1=Vector([1,4,5])
v2=Vector([2,2,2])
print(v1+v2,v1*v2)
v3=Vector([1,2])
print(len(v3))
