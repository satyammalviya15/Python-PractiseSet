# 6. Write __str__() method to print the vector as follows: 7i + 8j +10k Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v = Vector([7, 8, 10])
print(v)
