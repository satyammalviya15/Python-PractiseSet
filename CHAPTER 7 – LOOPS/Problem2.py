# 2. Write a program to greet all the person names stored in a list l and which start with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if i.startswith("S"):
        print("Hello!",i)