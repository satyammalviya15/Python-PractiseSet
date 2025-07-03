# 1. Write a program to find the greatest of four numbers entered by the user.
numlist = []
for i in range(4):
    a = int(input(f"Enter Number{i+1} : "))
    numlist.append(a)
print(max("The Maximum Number is ",numlist))