import random                                                                  # นำเข้า random

stick = int(input("How many sticks in the pile?  "))                           # รับค่า stick
print("There are", stick, "sticks in the pile.")
name = input("What is your name?  ")                                           # รับค่าชื่อผู้เล่น
turn = "C"                                                                     # ให้ turn = C เพื่อให้คอมเล่นก่อน

def bot_take(stick):                                                           # สร้างฟังก์ชั่นการหยิบไม้ของคอม
    
    if ((stick-1)%3 == 1):                                                     # ถ้า (stick-1)%3 == 1 ให้คอมหยิบ 1
        bot = 1
    elif ((stick-1)%3 == 2):                                                   # ถ้า (stick-1)%3 == 2 ให้คอมหยิบ 2
        bot = 2
    else:                                                                      #นอกเหนือจากนั้นให้สุ่มหยิบระหว่าง 1,2
        bot = random.randint(1,2)
    
    return bot

while stick>0:                                                                 # ถ้ายังมีstick อยู่ให้ทำต่อไปเรื่อยๆ
    
    if turn == "P":                                                            # ถ้า TURN = P ผู้เล่นได้หยิบไม้
        take = int(input(name+", how many sticks you will take(1 or 2). = "))  # รับจำนวนที่ต้องการหยิบ
        
        if (take > 0) and (take <= 2):
            if stick < take:                                                   #เช็คว่ามีไม้พอให้หยิบไหม
                print("There are not enough sticks to take.")
      
            else: 
                stick = stick - take                                           #นำไม้ที่หยิบออกกอง
                turn = "C"                                                     #สลับให้คอมเล่น
                if stick ==0:                                                  # เช็คว่าหยิบไม้เป็นคนสุดท้ายหรือไม่ถ้าใช่จะแพ้
                    print(name,"pick the last stick in the pile.")
                    print(name,"Lose")
                else:
                    print("There are",stick,"sticks in the pile.")             #ถ้าหยิบแล้วยังเหลืออยู่ให้โชว์ว่าเหลือstickอีกกี่ไม้
    
        elif take > 2:                                                         #ถ้าหยิบมากกว่า 2 ให้เตือนว่าหยิบมากกว่า 2 ไม่ได้
            print("No! you cannot take more than 2 sticks.")
    
        else:                                                                  #แจ้งเมื่อหยิบไม้น้อยกว่า 1 ว่าไม่สามารถทำได้
            print("No! you can't take less than 1 stick.")

    else:                                                                      # turn คอมเล่น
        bot = bot_take(stick)                                                  #เรียกใช้ function หยิบไม้ของคอม
        
        if stick < bot:                                                        # กรณี คอมหยิบไม้มากกว่าจำนวนไม้ที่เหลือ บังคับให้หยิบไม้ที่เหลือทั้งหมด
            bot = stick
            stick = stick - bot
            print("Bot take = ",bot)
            turn = "P"                                                         #สลับไปที่turnผู้เล่น
            if stick == 0:
                print("Bot pick the last stick in the pile.")                  #เมื่อคอมหยิบไม้แล้วไม้ในกองเท่ากับ 0 ให้คอมแพ้เกม
                print("Bot Lose")
                print("Congratulation",name+". You win!")
            else:
                print("There are",stick,"sticks in the pile.")           
        else:                                                                  #กรณีเมื่อเหลือไม้ให้หยิบ
            stick = stick - bot
            print("Bot take = ",bot)
            turn = "P"
            if stick == 0:
                print("Bot pick the last stick in the pile.")
                print("Bot Lose")
                print("Congratulation",name+". You win!")
            else:
                print("There are",stick,"sticks in the pile.")
