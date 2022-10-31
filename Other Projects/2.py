# Create the Rock, Paper and Scissors game with Python, we need to take the user’s choice 
# and then we need to compare it with the computer choice which is taken using the random module 
# in Python from a list of choices, and if the user wins, then the score will increase by 1.
# User: Rock, Paper or Scissors?         User: Rock, Paper or Scissors?
# CPU: rock                              CPU: paper
# Tie                                    You win! Paper covers Rock
# User: Rock, Paper or Scissors?         Rock, Paper or Scissors?
# CPU: scissors                          End the game
# You lose… Rock smashes Scissors        Final Scores:
# CPU:1           Hint: Make use of random module to design the game
# User:1
import random

print("Welcome to RPS")
uc = input("Enter either r or p or s\n")
cc = ["r","p","s"]
cs = random.choice(cc)
print(f'user choice is {uc} and pc choice is {cs}')


