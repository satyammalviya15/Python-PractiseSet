# 8. Write a program to make a copy of a text file “poem.txt”

with open("poem.txt", "r") as f:
    content = f.read()

with open("poems.txt", "w") as f:
    f.write(content)