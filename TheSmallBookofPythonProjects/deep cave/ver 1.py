import random
from pynput.keyboard import Key, Listener
#wrong ----------------------------------------
def on_press(key):
    keys_pressed = set()
    if key == Key.ctrl:
        keys_pressed.add(key)
    if key.char == 'c':
        keys_pressed.add(key)

    if

def on_release(key):
    print(key)
    if  key == '\x03':
        # Stop listener
        print("here")
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


#---------------------------
#todo: Track currently pressed keys in a set.
# In on_press, if Control is pressed, add to set.
# If 'c' key is pressed and control is in pressed keys, then call sys.exit() or stop listener.
# Implement on_release to remove keys from the pressed set.
# This way we can detect Ctrl+C combination correctly.



gapWidth = 12
WIDTH = 80

while True:

    leftWidth  = random.randint(6, 12)
    print(f"{(leftWidth) * '#'}{gapWidth*' '}{( WIDTH - gapWidth - leftWidth) * '#'}")
