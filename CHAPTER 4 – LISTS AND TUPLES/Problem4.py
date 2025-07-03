# 4. Write a program to sum a list with 4 numbers.
a=[1,2,3,4,5]
total = 0
for num in a:
    total += num
print("Sum using for-each loop:", total)

# Method 3: Using built-in sum function
print("Sum using built-in sum():", sum(a))