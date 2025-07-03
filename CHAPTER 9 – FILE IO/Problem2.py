# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

def game():
    return "10"

game_score = game()

f = open("HI-score.txt","r")
high_score = f.read()
f.close()

f = open("HI-score.txt","w")
if int(game_score)>=int(high_score):
    f.write(game_score)
f.close()