import cv2

def GetImg(path):
    img = cv2.imread(path)
    return img

def ToGrayScale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

def showImg(name,img):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.imshow(name, img)