# author Khldun Said 
# Task Vscode task 

import pyautogui
from time import sleep

sleep(2)
pyautogui.press('win')
sleep(2)

pyautogui.write("vscode")
sleep(2)

pyautogui.press('enter')
sleep(2)

# pyautogui.hotkey ('ctrlleft','shiftleft','x')

#  try:
#     extention_icon_location = None
#     while extention_icon_location is None:
#         extention_icon_location = pyautogui.locateOnScreen('extension.png')
#         sleep(5)
# except pyautogui.ImageNotFoundException:
#     print("Image not found")
#     exit()

# pyautogui.click(extention_icon_location.left+10,extention_icon_location.top+30 )

# Easy way using vscode shortcuts

extensions= ["clangd","c++ testmate","c++ helper","cmake","cmake tools"]

for x in extensions:
    pyautogui.hotkey ('ctrlleft','shiftleft','x')
    sleep(2)
    pyautogui.press('backspace', presses= 15)
    sleep(2)
    pyautogui.write(x)
    sleep (5)
    install_icon= pyautogui.locateOnScreen('install.png')
    pyautogui.click(install_icon)
    sleep(10)
    pyautogui.move(100,100)
    sleep(2)
    
print("done")




 

