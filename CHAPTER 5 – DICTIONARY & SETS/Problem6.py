# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
a={}
for i in range(4):
    name = input("Enter Your Name : ")
    langauge = input("Enter Your Faovrite Language")
    a.update({name:langauge})
print(a.items())