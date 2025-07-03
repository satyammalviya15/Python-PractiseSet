# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class abc:
    a=1
object = abc()
object.a=0
print(abc.a)