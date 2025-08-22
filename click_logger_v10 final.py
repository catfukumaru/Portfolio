from pynput import keyboard, mouse
import pygetwindow as gw
import time

running = True
clicked = False
def on_click(x, y, button, pressed):
    if pressed:
        global clicked
        clicked = True
    if not pressed:
        clicked = False

def on_press(key):
    if key == keyboard.Key.esc:
        global running
        running = False
        
with keyboard.Listener(on_press=on_press) as listener, mouse.Listener(on_click=on_click) :
    while (running):
        for window in gw.getAllWindows():
            if clicked:
                if window.isActive:
                    print(window.title)
                
        time.sleep(0.5) # to prevent excessive CPU usage

listener.join()