import pyautogui as pg
import time
import numpy as np

stuck = False

def LoacteAndClick(filename, plus=0):
    obj = pg.locateOnScreen(r"C:\Users\PC\Desktop\DragonCity-Runner-Event-Player\trainobject" + f"\{filename}.png", grayscale=True, confidence=0.7)
    x_obj, y_obj = int(obj.left + np.clip(plus, plus - 5, plus + 5)), int(obj.top + np.clip(plus, plus - 5, plus + 5))
    pg.moveTo(x_obj, y_obj)
    time.sleep(np.clip(.3, .2, .35))
    pg.mouseDown()
    time.sleep(np.clip(0.3, .2, 0.4))
    pg.mouseUp()
    time.sleep(np.clip(2, 1, 2.25))

try:
    pg.getWindowsWithTitle("Dragon City")[0].maximize()
    while 1:
        try:
            try:
                error = pg.locateOnScreen(r"C:\Users\PC\Desktop\DragonCity-Runner-Event-Player\trainobject\error.png", grayscale=True, confidence=0.8)
                time.sleep(np.clip(2, 1.5, 2.25))
                LoacteAndClick("close")

                LoacteAndClick("egg", 100)

                LoacteAndClick("hatchegg")

                LoacteAndClick("sell", 15)

                LoacteAndClick("sellconfirm", 15)
            except:
                heart = pg.locateOnScreen(r"C:\Users\PC\Desktop\DragonCity-Runner-Event-Player\trainobject\heart.png",
                                        grayscale=True, confidence=0.8)
                x_heart, y_heart = int(heart.left + np.clip(15, 10, 20)), int(heart.top + np.clip(15, 10, 20))
                px_color = pg.pixel(x_heart, y_heart)

                if px_color == (232, 54, 103) or stuck:
                    pg.moveTo(x_heart, y_heart)
                    time.sleep(np.clip(.3, .2, .35))
                    pg.mouseDown()
                    time.sleep(np.clip(0.225, .2, 0.4))
                    pg.mouseUp()
                    time.sleep(np.clip(2, 1.5, 2.25))

                    LoacteAndClick("den", 50)

                    LoacteAndClick("rebreed", 15)

                    LoacteAndClick("breed", 15)

                    LoacteAndClick("close")

                    time.sleep(np.clip(3.5, 3, 4))
                    LoacteAndClick("egg", 100)

                    LoacteAndClick("hatchegg")

                    LoacteAndClick("sell", 15)

                    LoacteAndClick("sellconfirm", 15)

                    stuck = False

        except Exception as e:
            print(e)

except:
    print("Dragon city not available")