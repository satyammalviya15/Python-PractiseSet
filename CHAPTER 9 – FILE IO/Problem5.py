# 5. Repeat program 4 for a list of such words to be censored.

censored_list = ["star","dark","little"]

with open("poem.txt", "r") as f:
    content = f.read()

for i in censored_list:
    content = content.replace(i, "#####")

with open("poem.txt", "w") as f:
    f.write(content)
