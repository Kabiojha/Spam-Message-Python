import pyautogui as spam
import time

def spammsg():
    limit = input("Enter the number of message :")
    msg = input("The message :")
    i = 0
    print("You have 5 seconds to go to your messenger and click !")
    time.sleep(5)  
    while i < int(limit):
        time.sleep(0) #add delay to your message
        spam.typewrite(msg)
        spam.press('Enter')
        i += 1
        
spammsg()