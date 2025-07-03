# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:“The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter Your Name: ")
marks = int(input("Enter Your Marks: "))
phone = int(input("Enter Your Mobile Number: "))
print("The name of student is {},his marks are {} and phone number is {}".format(name,marks,phone))