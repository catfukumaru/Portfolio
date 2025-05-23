
import random

def cave():
    gapWidth = 12
    WIDTH = 80

    while True:
        try:
            leftWidth = random.randint(6, 12)
            print(f"{(leftWidth) * '#'}{gapWidth * ' '}{(WIDTH - gapWidth - leftWidth) * '#'}")
        except KeyboardInterrupt:
            break


cave()