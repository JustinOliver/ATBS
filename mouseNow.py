#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui
from time import sleep

print('Press Crtl-c to quit or move mouse to upper left')

try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' +str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' +str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr)#, end='')
        sleep(5)
        #print('\b' * len(positionStr), end ='', flush=True)
        
        

except KeyboardInterrupt:
    print('\nDone.')
    
