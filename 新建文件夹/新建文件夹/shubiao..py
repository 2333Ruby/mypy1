import pyautogui
from time import sleep
pyautogui.FAILSAFE = False
try:
    while True:
        x, y = pyautogui.position()
        posi = 'x:' + str(x).rjust(4) + ' y:' + str(y).rjust(4)
        print('\r', posi, end='')
        sleep(0.5)
except KeyboardInterrupt:
    print('Quit!')
