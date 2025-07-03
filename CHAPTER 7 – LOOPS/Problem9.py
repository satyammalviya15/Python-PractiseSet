# 9. Write a program to print the following star pattern:
'''markdown
Copy
Edit
* * *
*   *     for n = 3
* * *'''
n=3
for i in range(n):
        print("* ",end="")
print("")
for j in range(n-2):
    print("* ",end="")
    for l in range(n-2):
        print("  ",end="")
    print("* ",end="")
    print("")
for k in range(n):
        print("* ",end="")