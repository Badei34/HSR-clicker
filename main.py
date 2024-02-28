from time import sleep
import random
import pyautogui as pgui
import keyboard as key
import vgamepad as vg

gamepad = vg.VX360Gamepad()

global in_dialogue
in_dialogue = False


def wait(): # Waits for random interval between 0, 0.3 and 0.6, 0.9 seconds
    a = random.uniform(0, .3)
    b = random.uniform(.6, .9)
    sleep(random.uniform(a, b))


def press_xbox(): # Performs A button press on xbox controller
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    sleep(.1)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()


print("Press 'enter' to start the script")
print("Press '1' to exit script.")
print("Press '2' to pause/unpause script.")

key.wait('enter')
print("Starting...")

while True: 
    sleep(3)
    if key.is_pressed('1'): # Exit
        print("Exiting...")
        exit()
    
    if key.is_pressed('2'): # Pause
        print("Script paused.")
        sleep(2)
        key.wait('2')
        print("Script unpaused.")
        sleep(2)
    
    try:
        pgui.locateOnScreen("cont.png", confidence=0.8)
        print("In dialogue.")
        in_dialogue = True
        
        while in_dialogue: # If in dialogue continue clicking
            try:
                pgui.locateOnScreen("cont.png", confidence=0.8)
                print("Clicking")
                press_xbox()
                wait()
            except: # If not in dialogue exit clicking loop and continue searching
                print("Not in dialogue.")
                in_dialogue = False
    
    except:
        print("Searching and waiting...")