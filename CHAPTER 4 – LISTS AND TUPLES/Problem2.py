# 2. Write a program to accept marks of 6 students and display them in a sortedmanner
students=[]
for i in range(6):
    student=input(f"Student {i+1} :")
    students.append(student)
students.sort()
print("This is The Marks of student in sortedmanner\n",students)
print(students.index(2))