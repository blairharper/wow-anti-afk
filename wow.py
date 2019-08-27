import pyautogui
from win32gui import GetWindowText, GetForegroundWindow
import time
import random
wowTitle = "World of Warcraft"
starttime=time.time()
keys = ['left', 'right', 'up', 'down', 'space']
while True:
 currentWindow = GetWindowText(GetForegroundWindow())
 key = random.randint(0, 4)
 if(currentWindow == wowTitle):
     print("Current window is WoW... pressing key: " + keys[key])
     pyautogui.press(keys[key])
 interval = random.randint(1, 120)
 time.sleep(interval - ((time.time() - starttime) % interval))

