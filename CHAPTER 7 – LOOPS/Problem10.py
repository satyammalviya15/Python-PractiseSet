# 10. Write a program to print the multiplication table of n using for loop in reversed order.
num=int(input("Enter The num for multiplication table : "))
for i in range(num*10,num-1,-num):
    print(i)