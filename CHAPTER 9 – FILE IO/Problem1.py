# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
with open("poem.txt") as f:
    content = f.read()  # Reads the entire file
    if "twinkle" in content:
        print("Found at index:", content.index("twinkle"))
    else:
        print("The word 'twinkle' is not found.")
