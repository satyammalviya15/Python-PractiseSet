# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not present, a message without exiting the program must be printed prompting the same.

try:
    with open("poem.txt","r")as poem,open("poems.txt","r")as poems,open("log.txt","r")as logfile:
        pass
except Exception as e:
    print(e)