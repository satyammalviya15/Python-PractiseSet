# 4. Write a program to filter a list of numbers which are divisible by 5.

a=[i for i in range(1,50)]

print(list(filter(lambda i:i%5==0,a)))
print(list())