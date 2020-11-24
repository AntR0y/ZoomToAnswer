from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
import pyperclip

# Press and release space
def openChat():
    # Type a lower case A; this will work even if no key on the
    # physical keyboard is labelled 'A'
    #keyboard.press(Key.cmd.value)
    #keyboard.press(Key.shift)
    keyboard.press(Key.alt)
    keyboard.press('h')
    keyboard.release('h')
    keyboard.release(Key.alt)
    #keyboard.release(Key.shift)
    #keyboard.release(Key.cmd.value)

    #i = 0
    #while i < 3:
    #    i += 1
    #    keyboard.press(Key.tab)
    #    keyboard.release(Key.tab)

    time.sleep(2)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)