import pyautogui as bot
import time
import keyboard

time.sleep(3)


controls = """
Controls/Commands
####################
Modes: Afk and LVLUP
Press: (ctrl) to change modes
####################

"""




    
while True:
    if keyboard.is_pressed('x'):
        break
    elif keyboard.is_pressed('space'):
        print("Clicker paused.")
        input("Press enter to unpause.")
        print("Unpausing in....")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
    else:
        pass
    
    bot.click(interval=0.009)
