# 4. Write a program to find whether a given username contains less than 10 characters or not.
username = input("Enter Your Name : ")
namelenth = len(username)
if(namelenth<10):
    print("Username contains less than 10 characters")
else:
    print("Success")