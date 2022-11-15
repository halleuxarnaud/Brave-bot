import pyautogui
import time
import os

while(1):
    i = 0
    k = 0
    while(i <= 10):
        os.startfile('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe')
        time.sleep(5)
        while(k <= 10):
            pyautogui.hotkey('ctrl', 'r')
            time.sleep(5)
            k = k + 1
        k = 0
        pyautogui.hotkey('alt', 'f4')
        i = i + 1
    i = 0
    os.startfile('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe')
    time.sleep(3100)
    pyautogui.hotkey('alt', 'f4')
