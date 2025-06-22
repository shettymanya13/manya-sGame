'''
1 is for snake
-1 is for water 
0 for gun
'''
import random

computer = random.choice([-1,0,1])
youstr = (input("enter your choice : "))
youDict = {"s":1, "w": -1, "g": 0}
reverseDict = {1 : "snake", -1 : "water", 0 : "gun"}
you = youDict[youstr]

print(f"you chose {reverseDict[you]} \ncomputer chose :{reverseDict[computer]}")

if(computer == you):
    print("draw")
else:

    if(computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("you loose ")
    elif(computer == 1 and you == -1):
        print("you loose !")
    elif(computer == 1 and you == 0):
        print("you win 1!")
    elif(computer == 0 and you == 1):
        print("you loose!")
    elif(computer == 0 and you == -1):
        print("you win !")
    else:
        print("some thing went wrong ")
    print("end of this round ")



# This program can also be written as :

'''
if(computer - you) == -1 or (computer-you) == 2):
    print("you loose !")
else:
    print("you win!")
'''

# the above program is less readable and short form of the game . 
