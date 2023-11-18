import cv2 as cv
import numpy as np

# Data
gameplay_img = cv.imread("./trainobject/general.png", cv.IMREAD_UNCHANGED)
big_obstacle = cv.imread("./trainobject/big.png", cv.IMREAD_UNCHANGED)
big_obstacle_2 = cv.imread("./trainobject/big2.png", cv.IMREAD_UNCHANGED)
small_obstacle = cv.imread("./trainobject/small.png", cv.IMREAD_UNCHANGED)
small_obstacle_2 = cv.imread("./trainobject/small2.png", cv.IMREAD_UNCHANGED)
dragon = cv.imread("./trainobject/dragon2.png", cv.IMREAD_UNCHANGED)

threshold = .50

current_obstacle = dragon.astype(np.uint8)
gameplay_img = gameplay_img.astype(np.uint8)

result = cv.matchTemplate(gameplay_img, current_obstacle, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

w = current_obstacle.shape[1]
h = current_obstacle.shape[0]

yloc, xloc = np.where(result >= threshold)

for (x,y) in  zip(xloc,yloc):
    cv.rectangle(gameplay_img, (x,y), (x+w, y+h), (0.255,255), 2)

cv.imshow("Gameplay", gameplay_img)
cv.waitKey()
cv.destroyAllWindows()
