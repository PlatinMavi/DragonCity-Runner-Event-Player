import cv2 as cv 
import numpy as np

threshold = .5
upgrade_image = cv.imread("./trainobject/small.png", cv.IMREAD_COLOR)

def detect(screenshot):
    result = cv.matchTemplate(screenshot, upgrade_image, cv.TM_CCOEFF_NORMED)
    # min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    w = upgrade_image.shape[1]
    h = upgrade_image.shape[0]

    yloc, xloc = np.where(result >= threshold)

    for (x,y) in  zip(xloc,yloc):
        cv.rectangle(screenshot, (x,y), (x+w, y+h), (0.255,255), 2)

    return screenshot