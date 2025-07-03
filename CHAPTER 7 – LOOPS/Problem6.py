# 6. Write a program to calculate the factorial of a given number using for loop.
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

num = int(input("Enter Number for find Factorial"))
print(factorial(num))