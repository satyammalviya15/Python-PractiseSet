#1. Write a program to print multiplication table of a given number using for loop.
num = int(input("Give a num for create Table of it : "))
for i in range(num,num*10+1,num):
    print(i)