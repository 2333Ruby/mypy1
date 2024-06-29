import pyautogui
from time import sleep
print(pyautogui.size())
print(pyautogui.position())
# pyautogui.dragTo(900, 900, duration=1)
sleep(2)
left, top, width, height = pyautogui.locateOnScreen('点赞.png')
center = pyautogui.center((left, top, width, height))
pyautogui.click(center)
# pyautogui.click(1500, 900)