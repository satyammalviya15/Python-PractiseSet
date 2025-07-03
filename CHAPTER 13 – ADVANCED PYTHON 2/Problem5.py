# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce

nums=[i for i in range(1,10)]
max=reduce(lambda x,y:x if x>y else y , nums)
print(max)