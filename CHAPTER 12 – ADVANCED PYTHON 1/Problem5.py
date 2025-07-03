# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
num = int(input("Please Enter a Number For Multiplication Table : "))
list=[i for i in range(num,num*10+1,num)]

with open("Tables.txt","w") as f:
    f.write(str(list))