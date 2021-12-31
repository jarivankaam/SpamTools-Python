#chat spam bot
import string
import pyautogui
import time
import os

running = True

while running:
    print(""""
    ██████ ██   ██  █████  ████████     ███████ ██████   █████  ███    ███ ██████   ██████  ████████ 
    ██      ██   ██ ██   ██    ██        ██      ██   ██ ██   ██ ████  ████ ██   ██ ██    ██    ██    
    ██      ███████ ███████    ██        ███████ ██████  ███████ ██ ████ ██ ██████  ██    ██    ██    
    ██      ██   ██ ██   ██    ██             ██ ██      ██   ██ ██  ██  ██ ██   ██ ██    ██    ██    
     ██████ ██   ██ ██   ██    ██        ███████ ██      ██   ██ ██      ██ ██████   ██████     ██    
                                                                                                     
    Disclaimer: This script was made to mess with people on apps like discord and to mess with people on
    chat sites don't use it to spread malicious messages or to annoy your teachers during online classes!                                                                                             
    """)


    print("[1] Spam bot")
    print("[2] Chat Message bot")

    choice = int(input("[?]:"))
    if choice == 1:
        os.system('cls')
        i = 0
        choice2 = input("enter word or phrase you want to spam: ")
        count = int(input("how many times do you want to spam?(warning don't spam over 50 times!)"))
        print("You have 5 seconds place your cursor in the desired chat box")
        time.sleep(5) #5 second pause
        for i in range(count):
            pyautogui.typewrite(choice2)
            pyautogui.press("enter")
            time.sleep(0.1)
            os.system('cls')
            i = i + 1
            print(f"spammed {i} times")
        print(f"spammed: {choice2} {count} times" )

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
    else:
        print("type something in")

    stop = input("druk op enter om door te gaan of op x om te stoppen:\n")
    if(stop == "X" or stop == "x"):
        running = False