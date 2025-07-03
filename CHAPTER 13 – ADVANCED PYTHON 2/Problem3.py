# 3. A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

list=[i for i in range(7,71,7)]
result=""
for i in list:
    result+=f"{i}\n"
print(result)