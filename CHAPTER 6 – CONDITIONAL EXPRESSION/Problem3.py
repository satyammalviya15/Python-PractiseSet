# 3. A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
comment = input("Enter Your Comment: ").lower()
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]
is_spam = False

for keyword in spam_keywords:
    if keyword in comment:
        is_spam = True
        break

if is_spam:
    print("It's a Spam Comment")
else:
    print("It's a Normal Comment")

