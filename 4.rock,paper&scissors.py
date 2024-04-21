import random
box=["rock","paper","scissor"]

computer_win=0
user_win=0
tie=0
print("Welcome to rock paper scissor....")
print('''
RULES:
     ⨀ User will choose one of three from rock,paper &scissor
     ⨀ Rock beats scissor, scissor beats paper , paper beats rock...
     ⨀ Total score will be displayed at end of game ..
''')
while True:
    user_value=input("Enter (rock/paper/scissor):")

    if user_value not in box:
        continue
    guess=random.randint(0,2)
    computer_value=box[guess]
    print(f"You choosed      : {user_value}")
    print(f"Computer choosed : {computer_value}")
    if user_value=="rock" and computer_value=="scissor":
        print(">>You won!!!")
        user_win+=1
    elif user_value=="paper" and computer_value=="rock":
        print(">>You won!!!")
        user_win+=1
    elif user_value=="scissor" and computer_value=="paper":
        print(">>You won")
        user_win+=1
    elif user_value==computer_value:
        print(">>Tie!!")
        tie+=1
    else:
        print(">>You lost!,Computer won..")
        computer_win+=1
    print("") 
    val=input("You want to continue(y/n)?")
    print("") 
    if val=="n":
        break
    
print(f'''>>>Total games:{user_win+computer_win+tie}
>>>You won {user_win} games.
>>>Computer won {computer_win} games
>>>Ties:{tie}.''')
print("Thanks for playing")