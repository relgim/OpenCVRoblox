import os
import keyboard
from time import time, sleep
import pyautogui
from mss import mss
import cv2 as cv
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


picture_path = os.getcwd() + '\ProjectOne\Roblox\Pictures'
file_path2 = os.path.join(picture_path, 'Goku.png')
file_path = cv.imread(file_path2, cv.IMREAD_UNCHANGED)

monitor = {
        'top': 0, 
        'left':0, 
        'width':1920, 
        'height':1080
}

sct = mss() #Screen Shot of monitor

while 1 :
    screen = np.array(sct.grab(monitor)) #Define Size of Monitor with the screen shot -> Returns an Array (By Numpy) as Screen / scr
    screen_remove = screen[:,:,:3] #Remove Alpha

    result = cv.matchTemplate(screen_remove, file_path, cv.TM_CCOEFF_NORMED) #Looks for Potential match with algorithm
    #_, max_val, _, max_loc = cv.minMaxLoc(result) #Gets the cordinate
    #screen = scr.copy()

    threshold = 0.85
    locations = np.where(result >= threshold)
    if locations :
        file_path_w = file_path.shape[1]
        file_path_h = file_path.shape[0]

        for loc in locations :
            top_left = loc
            bottom_right = (top_left[0] + file_path_w, top_left[1] + file_path_h) 
            cv.rectangle(screen, top_left, bottom_right, (5,5,5), 5) #Looks for Potential match with algorithm

        cv.imshow('Screen Shot', screen)
        cv.waitKey()

    if keyboard.is_pressed('q'):
        break