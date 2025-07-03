# Project1: Build Snake-Water-Gun Game Like Stone-Paper-Sesor

import random

option=["S","W","G"]

print("Let's Play Snake,Water & Gun Game")
rounds = int(input("Enter No of Rounds : "))

for i in range(rounds):
    print(f"Round {i+1}")
    print("Snake -'S'")
    print("Water -'W'")
    print("Gun   -'G'")
    useroption=input("Enter Your Choice : ").upper()
    computeroption=random.choice(option)
    if(useroption==computeroption):
        print("Computer Chose :",computeroption)
        print("It's a Draw")
    elif((useroption=='S' and computeroption=="W")or
         (useroption=='W' and computeroption=="G")or
         (useroption=='G' and computeroption=="S")):
        print("Computer Chose :",computeroption)
        print(f"You Win Round{i+1}")
    elif((useroption=='W' and computeroption=="S")or
         (useroption=='G' and computeroption=="W")or
         (useroption=='S' and computeroption=="G")):
        print("Computer Chose :",computeroption)
        print(f"You Loss Round{i+1}")