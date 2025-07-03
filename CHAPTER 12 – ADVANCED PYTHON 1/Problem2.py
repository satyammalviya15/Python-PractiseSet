# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

list=[i for i in range(1,11)]

for index,i in enumerate(list,start=1):
    if(index==3 or index==5 or index==7):
        print(i)