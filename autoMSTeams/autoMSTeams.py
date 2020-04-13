import pyautogui
import time

print('Dam bao cua so them ID vao class trong MS Teams dang mo!')
time.sleep(5) #Thoi gian cho de quay lai MS Teams
file = open('listID.txt','r') #Mo file chua danh sach ID can them vao 
for id in file:
    pyautogui.typewrite(id,interval=0.0)
    time.sleep(2) #Thoi gian cho xu ly cho moi ID
    pyautogui.press('enter')

