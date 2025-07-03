# 5. Write a program which finds out whether a given name is present in a list or not.
namelist = ["satyam","shivam","sundram"]
name = input("Enter Your Name").lower()
if name in namelist:
    print("Login Sucessfully")
else:
    print("You are not in namelist")