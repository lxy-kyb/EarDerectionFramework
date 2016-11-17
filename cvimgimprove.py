import cv2

def improve(img):
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    cl2 = clahe.apply(cl1)
    return cl2