# 4. A file contains a word “star” multiple times. You need to write a program which replace this word with ##### by updating the same file.

with open("poem.txt", "r") as f:
    content = f.read()

content = content.replace("star", "#####")

with open("poem.txt", "w") as f:
    f.write(content)
