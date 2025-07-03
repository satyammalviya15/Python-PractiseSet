# 4. Write a program to find whether a given number is prime or not.
num=int(input("Enter a Number For Checking Prime or not : "))
isprime=True
for i in range(2,num):
    if num%i==0:
        isprime=False
        break
if isprime==True:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")
    