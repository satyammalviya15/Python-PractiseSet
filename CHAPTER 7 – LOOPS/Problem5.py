# 5. Write a program to find the sum of first n natural numbers using while loop.
num=int(input("Enter The nth Natural No : "))
i=0
sum=0
while i<num:
    sum+=i
    i=i+1
print(f"The Sum of First {num} natural numbers",sum)