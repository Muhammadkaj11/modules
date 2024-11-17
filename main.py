import random
options=["rock", "paper", "scissors"]
user_choice=input("chose rock,paper or scissors")
computer_choice=random.choice(options)
print("you chose",user_choice)
print("the computer chose",computer_choice)
if user_choice==computer_choice:
    print("it is a tie")
elif user_choice=="rock" and computer_choice=="scissors":
    print("rock smashes scissors so you win")
elif user_choice=="paper" and computer_choice=="rock":
    print("paper covers rock so you win")
elif user_choice=="scissors" and computer_choice=="paper":
    print("scissors cuts paper so you win")
else:
    print("you lose")