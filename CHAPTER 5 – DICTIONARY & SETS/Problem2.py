# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
num=set()
for i in range(8):
    num.add(input(f"Enter NO {i+1} : "))
print(num)