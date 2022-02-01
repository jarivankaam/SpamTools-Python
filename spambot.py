#chat spam bot
import string
import pyautogui
import time
import os
import passwordConfig as cfg

running = True

while running:
    print(""""
     ██████ ██   ██  █████  ████████     ███████ ██████   █████  ███    ███ ██████   ██████  ████████ 
    ██      ██   ██ ██   ██    ██        ██      ██   ██ ██   ██ ████  ████ ██   ██ ██    ██    ██    
    ██      ███████ ███████    ██        ███████ ██████  ███████ ██ ████ ██ ██████  ██    ██    ██ 
    ██      ██   ██ ██   ██    ██             ██ ██      ██   ██ ██  ██  ██ ██   ██ ██    ██    ██ 
     ██████ ██   ██ ██   ██    ██        ███████ ██      ██   ██ ██      ██ ██████   ██████     ██ tm
                                                                                                  
    Disclaimer: This script was made to mess with people on apps like discord and to mess with people on
    chat sites don't use it to spread malicious messages or to annoy your teachers during online classes!
    """)


    print("[1] Spam bot")
    print("[2] Chat Message bot")
    print("[3] Spam bot(with limits)")

    choice = int(input("[?]:"))
    if choice == 1:
        print("This option is password protected")
        password = cfg.password["password"]
        passwordInput = input("[🔒]:")
        if passwordInput == password:
            os.system('cls')
            i = 0
            choice2 = input("enter word or phrase you want to spam: ")
            count = int(input("how many times do you want to spam?(warning don't spam over 50 times!)"))
            print("You have 5 seconds place your cursor in the desired chat box")
            time.sleep(5) #5 second pause
            for i in range(count):
                pyautogui.typewrite(choice2)
                pyautogui.press("enter")
                time.sleep(0.1) # 0.1 second pause
                os.system('cls')
                i = i + 1
                print(f"spammed {i} times")
            print(f"spammed: {choice2} {count} times" )
        else: print(f"{passwordInput} is not the right password")    

    elif choice == 2:
        os.system('cls')
        choice2 = input("enter words or phrases you want to spam: ")
        count = int(input("how many times do you want to spam?(warning don't spam over 50 times!)"))
        print("You have 5 seconds place your cursor in the desired chat box")
        time.sleep(5) #5 second pause
        i = 0
        for i in range(count):
            time.sleep(1)
            pyautogui.typewrite(choice2)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("escape")
            pyautogui.press("escape")
            time.sleep(0.2)
            i = i + 1
            os.system('cls')
            print(f"spammed {i} times")
        print(f"spammed: {choice2} {count}  times" )
    elif choice == 3:
        os.system('cls')
        choice3 = input("enter words or phrases you want to spam: ")
        count = int(input("how many times do you want to spam?(Max. 25 times)"))
        if count <= 25:
            print("You have 5 seconds place your cursor in the desired chat box")
            time.sleep(5) #5 second pause
            i = 0
            os.system('cls')
            
            choice2 = input("enter word or phrase you want to spam: ")
            count = int(input("how many times do you want to spam?(warning don't spam over 50 times!)"))
            print("You have 5 seconds place your cursor in the desired chat box")
            time.sleep(5) #5 second pause
            for i in range(count):
                pyautogui.typewrite(choice3)
                pyautogui.press("enter")
                time.sleep(0.1) # 0.1 second pause
                os.system('cls')
                i = i + 1
                print(f"spammed {i} times")
            print(f"spammed: {choice3} {count} times" )
        elif count > 25: print(f"You chose {count} however you can't spam more than 25 times")   
        else: "Count can't be empty"
    else: "type the right things buddy"
    
    stop = input("druk op enter om door te gaan of op x om te stoppen:\n")
    if(stop == "X" or stop == "x"):
        running = False
