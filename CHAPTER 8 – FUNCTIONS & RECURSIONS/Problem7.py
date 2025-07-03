# 7. Write a python function to remove a given word from a list and strip it at the same time.

def remove_word(word,list):
    if word in list:
        list.remove(word)

list=["satyam","shivam","sundrem","ram"]
remove_word("ram",list)
print(list)
        