# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class vector2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    
    def show(self):
        return(self.i,self.j)

class vector3D(vector2D):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        return(self.i,self.j,self.k)

v2=vector2D(1,2)
v3=vector3D(1,2,3)
print(v2.show(),v3.show())