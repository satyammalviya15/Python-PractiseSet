# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    add=0
    for i in range(n):
        add+=i
    return add
print(sum(5))