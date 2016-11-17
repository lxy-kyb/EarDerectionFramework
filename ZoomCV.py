import cv2
import os

def Scale(image, m,n):
    resized_image = cv2.resize(image, (m, n))
    return resized_image