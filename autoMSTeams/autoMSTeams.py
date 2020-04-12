import pyautogui
import time
import keyboard
import os

# pyautogui.PAUSE = 10
# time.sleep(5) 

# text_to_print='default_predefined_text'
# shortcut = 'cmd+b' #define your hot-key
# print('Hotkey set as:', shortcut)

# def on_triggered(): #define your function to be executed on hot-key press
#     print(text_to_print)
#     #write_to_textfield(text_to_print) #<-- your function
# keyboard.add_hotkey(shortcut, on_triggered) #<-- attach the function to hot-key
# print("Press ESC to stop.")
# keyboard.wait('esc')

print('Ensure that the MS Teams window is active!')
time.sleep(5) 
file = open('listID.txt','r')
for id in file:
    pyautogui.typewrite(id,interval=0.0)
    time.sleep(2) 
    pyautogui.press('enter')

# id = '3200319068'
# pyautogui.typewrite(id,interval=0.0)
# time.sleep(2) 
# pyautogui.press('enter')
# # p = pyautogui.position()
# # pyautogui.click(p[0],p[1]+5)

# # for i in range(10): # Move mouse in a square.
# #    pyautogui.moveTo(100, 100, duration=0.25)
# #    pyautogui.moveTo(200, 100, duration=0.25)
# #    pyautogui.moveTo(200, 200, duration=0.25)
# #    pyautogui.moveTo(100, 200, duration=0.25)