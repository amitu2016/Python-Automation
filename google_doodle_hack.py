import pyautogui
import time


pyautogui.PAUSE = 0.01
pyautogui.moveTo(1481,14,duration=1)
pyautogui.click()
pyautogui.moveTo(559,885,duration=1)
pyautogui.click()
pyautogui.moveTo(142,51,duration=1)
pyautogui.click()
pyautogui.write("Google doodle hurdle",interval=.1)
time.sleep(1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(247,312,duration=1)
pyautogui.click()
time.sleep(6)
pyautogui.moveTo(794,312,duration=1)
pyautogui.click()
time.sleep(1)

for i in range(300):
    pyautogui.press('left')
    pyautogui.press('right')




