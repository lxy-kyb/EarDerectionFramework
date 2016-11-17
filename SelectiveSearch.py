import cv2
import random
import time

def RamdomRect(img):
    height, width, channels = img.shape
    for i in range(0, 30):
        print '<---Search Selective window width {0} height {1}---->'.format(random.randint(0, height), random.randint(0, width))
    xheight = random.randint(0, height)
    xwidth = random.randint(0, width)
    yheight = random.randint(0, height)
    ywidth = random.randint(0, width)
    tmp = img.copy()
    cv2.rectangle(tmp,(xwidth,xheight),(ywidth,yheight),(0,255,0),1)
    return tmp
