import cv2 as cv 
import numpy as np
from time import time
import win32gui
import win32ui
import win32con
import object

looptime = time()

# def list_window_names():
#     def winEnumHandler(hwnd, ctx):
#         if win32gui.IsWindowVisible(hwnd):
#             print(hex(hwnd), win32gui.GetWindowText(hwnd))
        
#     win32gui.EnumWindows(winEnumHandler, None)

# list_window_names()

def getScreenshot():
    
    w = 1920 # set this
    h = 1080 # set this
    windowname = "Dragon City"
    # windowname = None

    hwnd = win32gui.FindWindow(None, windowname)
    
    rect = win32gui.GetWindowRect(hwnd)
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    # hwnd = None

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h,w,4)

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    # img = img[...,:3]

    return np.ascontiguousarray(img[...,:3])

while(True):

    screenshot = getScreenshot()
    display = object.detect(screenshot)

    cv.imshow("Realtime", display)

    print(f"FPS : {str(1 / (time() - looptime))[:6]}")
    looptime = time()

    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
