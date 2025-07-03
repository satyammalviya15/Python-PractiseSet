# We are going to write a program that generates a random number and asks the user to guess it. If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.
#Hint: Use the random module.

import random

num=random.randrange(1,100)
win=False
attempt=0
print("Let's Play a Random Number Game")
while(win==False):
    usernum=int(input("The Num is : "))
    attempt+=1
    if usernum==num:
        print("You are Right The Number is",usernum)
        print("You are Win in",attempt,"attempt")
        win=True
    elif usernum>num:
        print("Lower Number Please")
    else:
        print("Higher Number Please")