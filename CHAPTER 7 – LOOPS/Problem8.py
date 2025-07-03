# 8. Write a program to print the following star pattern:
'''diff
Copy
Edit
*
**
***   for n = 3'''
for i in range(3):
    print("")
    for j in range(i+1):
        print("*",end="")