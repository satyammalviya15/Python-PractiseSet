# 9. Write a program to find out whether a file is identical & matches the content of another file.

with open("poem.txt","r") as f:
    content1 = f.read()

with open("poems.txt","r") as f:
    content2 = f.read()

if content1==content2:
    print("Files are Identical")
else:
    print("Files are not Identical")