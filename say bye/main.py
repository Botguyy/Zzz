#Code by HermanErKu
#Made in Python 3.9
import pyautogui
import Keyboard
import time

word = input(" NUKED BY ONI - @everyone ")  #asks what you want to spam
print("You will now get 6 seconds to get ready")  #you will get 6 seconds before it starts

def spam():
    for i in range(1000):  #how many times it spams the word
        pyautogui.typewrite(word)  #writes the words you want to spam
        time.sleep(0.5)  #waits 0,5 seconds | this is because a problem i found in discord where it just loaded, and all of the words gatheret in one big message
        pyautogui.press('enter')  #presses enter

time.sleep(6)  #waits the six seconds
spam()  #does the spamming
