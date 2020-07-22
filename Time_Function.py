import pyautogui
import time


x = time.time()
pyautogui.write("Hello, How are you ",interval=0.2)
y = time.time()
z = y-x
print(z)
