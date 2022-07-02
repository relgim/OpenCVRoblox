
import keyboard
from time import time, sleep
import pyautogui
from mss import mss
import cv2
from PIL import Image
import numpy as np


mon = {'top': 100, 'left':200, 'width':1600, 'height':1024}

sct = mss()

while 1:
    begin_time = time()
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    wood = cv2.imread('wood.jpg', cv2.IMREAD_UNCHANGED)
    
    result = cv2.matchTemplate(np.array(screen), wood, cv2.TM_CCOEFF_NORMED)
    
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    w = wood.shape[1]
    h = wood.shape[0]
    cv2.rectangle(np.array(screen), max_loc , (max_loc[0] +w , max_loc[1]+h), (0,255,255),2)
    cv2.imshow('test', np.array(screen) )



    print('This frame takes {} seconds.'.format(time()-begin_time))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break


#
#img = cv.imread('wood.jpg', cv.IMREAD_UNCHANGED)

#cv.imshow('Cat', img)

#cv.waitKey()