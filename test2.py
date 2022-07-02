
import keyboard
from time import time, sleep
import pyautogui
from mss import mss
import cv2
from PIL import Image
import numpy 


monitor = {
        'top': 100, 
        'left':200, 
        'width':1920, 
        'height':1080
}
dimensions_left = {
        'left': 290,
        'top': 600,
        'width': 150,
        'height': 250
    }

dimensions_right = {
        'left': 520,
        'top': 600,
        'width': 150,
        'height': 250
    }

sct = mss()

left = True
timeBean = False

goku = cv2.imread('goku2.png')
replay = cv2.imread('replay.png')
pink = cv2.imread('pink.png')

w = goku.shape[1]
h = goku.shape[0]

w1 = replay.shape[1]
h1 = replay.shape[0]

w2 = pink.shape[1]
h2 = pink.shape[0]

count = 0
count2 = 0

while 1:
    if timeBean :
        if time() - clock >= 545 :
            print('Time Bean')
            timeBean = False

    if left:
        scr = numpy.array(sct.grab(monitor))
        search = goku
    else:
        scr = numpy.array(sct.grab(monitor))
        search = replay

    scr = numpy.array(sct.grab(monitor))

    scr_remove = scr[:,:,:3]
    
    result = cv2.matchTemplate(scr_remove, search, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(f"G-Max Val: {max_val} Max Loc: {max_loc}")

    result2 = cv2.matchTemplate(scr_remove, pink, cv2.TM_CCOEFF_NORMED)
    _, max_val2, _, max_loc2 = cv2.minMaxLoc(result2)
    cv2.rectangle(scr, max_loc2, (max_loc2[0] + w2, max_loc2[1] + h2), (5,5,5), 5)
    print(f"Pink-Max Val: {max_val2} Max Loc: {max_loc2}")

    #if left :
    #    print(f"G-Max Val: {max_val} Max Loc: {max_loc} Max Val: {max_val}")
    #else :
    #    print(f"R-Max Val: {max_val} Max Loc: {max_loc} Max Val: {max_val}")
    src = scr.copy()
    if False and max_val > .38:
        if left:
            cv2.rectangle(scr, max_loc, (max_loc[0] + w, max_loc[1] + h), (5,5,5), 5)
        else:
            cv2.rectangle(scr, max_loc, (max_loc[0] + w1, max_loc[1] + h1), (5,5,5), 5)

    cv2.imshow('Screen Shot', scr)


    if False and 1800 >= max_loc[0] >= 1400 and  1000 >= max_loc[1] >= 800 and max_val > .35 and left == False: 

        if timeBean :
            count2 = count2 + 1
            print(f"Early Cancel :  {count2}")
            pyautogui.click(2060,50)
        else :
            count = count + 1
        print(f"R-Max Val: {max_val} Max Loc: {max_loc} Count: {count}")
        sleep(1)
        pyautogui.click(2060,150)
        sleep(10)
        left = not left

    if False and 700 >= max_loc[0] >= 550 and  100 >= max_loc[1] >= 0 and max_val > .45 and left: 
        print(f"G-Max Val: {max_val} Max Loc: {max_loc}")

        result2 = cv2.matchTemplate(scr_remove, pink, cv2.TM_CCOEFF_NORMED)
        _, max_val2, _, max_loc2 = cv2.minMaxLoc(result2)
        cv2.rectangle(scr, max_loc, (max_loc[0] + w2, max_loc[1] + h2), (5,5,5), 5)

        print(f"Pink-Max Val: {max_val2} Max Loc: {max_loc2}")

        sleep(50)

        pyautogui.click(2060,50)
        #sleep(545)
        #pyautogui.click(2060,50)

        clock = time()
        timeBean = True

        left = not left
    cv2.waitKey(1)

    if keyboard.is_pressed('q'):
        break