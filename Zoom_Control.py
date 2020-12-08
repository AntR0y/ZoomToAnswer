from sys import platform
from pynput.keyboard import Key, Controller
import pyperclip
keyboard = Controller()

# Press and release space
def openChat():
    # Open chat; shortcut differs based on operating system, assuming Windows and MacOS use for now
    if platform == 'win32':
        keyboard.press(Key.alt)
        keyboard.press('h')
        keyboard.release('h')
        keyboard.release(Key.alt)
    elif platform == 'darwin':
        keyboard.press(Key.cmd.value)
        keyboard.press(Key.shift)
        keyboard.press('h')
        keyboard.release('h')
        keyboard.release(Key.shift)
        keyboard.release(Key.cmd.value)
    else:
        keyboard.press(Key.cmd.value)
        keyboard.press(Key.shift)
        keyboard.press('h')
        keyboard.release('h')
        keyboard.release(Key.shift)
        keyboard.release(Key.cmd.value)
 
    # Paste result into chat and enter
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)