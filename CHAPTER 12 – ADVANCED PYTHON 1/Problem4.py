# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter The Value of a"))
    b = int(input("Enter The Value of b"))
    print(a/b)
except ZeroDivisionError:
    print("infinite by handling the ‘ZeroDivisionError’")