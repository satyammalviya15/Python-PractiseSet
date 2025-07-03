# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

num = int(input("Please Enter a Number For Multiplication Table : "))
list=[i for i in range(num,num*10+1,num)]
print(list)