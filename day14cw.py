#Rock paper scissors
#rule= paper>rock ,rock>scissors,scissors>paper
print("Rock paper scissors game")
print("Rule:Paper>rock, rock>scissors, scissors>paper")

import random
computer = random.choice(["rock","paper","scissors"])

user = input("Enter your choice: ")
print(user)
print(computer)

if(user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or(user == 'scissors' and computer == 'paper'):
    print("user has won")
elif user == computer:
    print("Game is Tie")
elif user not in ['rock','paper','scissors']:
    print("Invalid words")
else:
    print("Computer won")


#import =inbuilt and random = randomly print
#choice method ho like append,update 
