import random
num=random.randint(1,10)
user_choice=int(input("give your best choice:"))
if user_choice==num:
    print("you win and you guessed correctly")
else:
    print("you lose and you guessed wrongly")
    print("the real answer is",num)