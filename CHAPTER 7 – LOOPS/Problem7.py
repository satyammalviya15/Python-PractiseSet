# 7. Write a program to print the following star pattern:
'''
markdown
Copy
Edit
  *
 ***
*****   
for n = 3'''
n = 3
for i in range(n):
  print("")
  for j in range(n-i-1):
    print(" ",end="")
  for k in range(2*i+1):
    print("*",end="")
for i in range(n,0,-1):
  print("")
  for k in range(n-i):
    print(" ",end="")
  for j in range(2*i-1):
    print("*",end="")
# 5 3 1