# 1. Program to store seven fruits entered by the user in a list
fruits = []

print("Enter 7 fruit names:")

for i in range(7):
    fruit = input(f"Fruit {i+1}: ").title()
    fruits.append(fruit)

print("\nList of fruits entered:")
print(fruits)
