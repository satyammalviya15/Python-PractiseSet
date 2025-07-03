# 5. Write a python function to print first n lines of the following pattern:
# ***
# **
# *
def pattern(n):
    for i in range(n):
        print("")
        for j in range(n-i):
            print("*",end="")
pattern(5)