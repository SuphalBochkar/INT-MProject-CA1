# Dice Roller And Score
    # Design a project where as an input student will give a static number (between 1 to 6) 
    # and then roll the dice which randomly generate some value between 1 to 6. The winning 
    # situation arrives when the given static/fixed number exactly same to the number came after rolling the dice.
    # User can play the game as many numbers of times he wants until user wants to exit, 
    # and whenever winning situation occur some scores must be given to the user, 
    # and these scores goes on adding if user play this game multiple number of times.
    # Note: Dice contains face value’s (1 to 6)
    # Hint: Make use of random.randint() function
import random
user_choice=int(input("Dice Number:"))
if user_choice < 0:
    print("invalid")
pc_choice=random.randint(1,6)



