import pyautogui
import winsound
from time import sleep
from Buyer import Scanner

result = False
buy_price = 900

print("Starting script...", flush=True)
sleep(3)

# Loop f5 keystrokes to refresh Flea Market
while True:
    pyautogui.press('f5')
    winsound.Beep(587, 120) ; winsound.Beep(784, 120)
    sleep(0.5)
    result = Scanner(buy_price)

    if not result: # exits on first purchase
        break

    sleep(4) 


#  # Extra references
# pyautogui.press('space')
# pyautogui.write('hello world!', 0.25)
# screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
# currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.


print("\nScript ended.")