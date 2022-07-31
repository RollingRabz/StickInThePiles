import random#### นำเข้า random

stick = int(input("How many sticks in the pile?  "))
print("There are", stick, "sticks in the pile.")
name = input("What is your name?  ")
turn = "C"

def bot_take(stick):
    
    if ((stick-1)%3 == 1):
        bot = 1
    elif ((stick-1)%3 == 2):
        bot = 2
    else:
        bot = random.randint(1,2)
    
    return bot

while stick>0:
    
    if turn == "P":
        take = int(input(name+", how many sticks you will take(1 or 2). = "))
        
        if (take > 0) and (take <= 2):
            if stick < take:                 
                print("There are not enough sticks to take.")
      
            else: 
                stick = stick - take
                turn = "C"
                if stick ==0:
                    print(name,"pick the last stick in the pile.")
                    print(name,"Lose")
                else:
                    print("There are",stick,"sticks in the pile.")
    
        elif take > 2:
            print("No! you cannot take more than 2 sticks.")
    
        else:
            print("No! you can't take less than 1 stick.")

    else:
        bot = bot_take(stick)
        
        if stick < bot:
            bot = stick
            stick = stick - bot
            print("Bot take = ",bot)
            turn = "P"
            if stick == 0:
                print("Bot pick the last stick in the pile.")
                print("Bot Lose")
                print("Congratulation",name+". You win!")
            else:
                print("There are",stick,"sticks in the pile.")           
        else:
            stick = stick - bot
            print("Bot take = ",bot)
            turn = "P"
            if stick == 0:
                print("Bot pick the last stick in the pile.")
                print("Bot Lose")
                print("Congratulation",name+". You win!")
            else:
                print("There are",stick,"sticks in the pile.")
