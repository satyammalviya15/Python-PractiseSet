# 6. Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
try:
    num = int(input("Enter Your Grade"))
    if num>90 and num<=100:
        print("Your Grade is Ex")
    elif num>80 and num<=90:
        print("Your Grade is A")
    elif num>70 and num<=80:
        print("Your Grade is B")
    elif num>60 and num<=70:
        print("Your Grade is C")
    elif num>=50 and num<=60:
        print("Your Grade is D")
    else:
        print("Your Grade is F")

except ValueError:
    print("Please Enter Integer Marks Only")
    