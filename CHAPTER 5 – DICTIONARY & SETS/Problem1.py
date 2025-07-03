# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
hindidictionary={
    "Aakh":"Eyes",
    "namaste":"hello",
    "kya":"what",
    "kyu":"why"
}
word=input("Enter Word for find English Meaning")
print(hindidictionary.get(word))