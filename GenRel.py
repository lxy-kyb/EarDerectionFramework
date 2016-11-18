import os
import cv2

path_txt = 'txt'
path_img = 'src'
path_train = 'x_train'

def GetXYScale(txtPath, x):    
    with open(txtPath, 'r') as file:
        for line in file.readlines():
            list_t = str(line).split(',')
            if int(list_t[0]) == x:
                return (int(list_t[3]),int(list_t[4]),int(list_t[5]),int(list_t[6]))

def GenTrain():
    list_img = os.listdir(path_img)
    for name in list_img:
        txtName = os.path.splitext(name)[0] + '.txt'
        txtPath = os.path.join(path_txt, txtName)
        if os.path.exists(txtPath):
            (x1,x2,y1,y2) = GetXYScale(txtPath, 1)
            print (x1,x2,y1,y2)
            fullpath = os.path.join(path_img, name)
            img = cv2.imread(fullpath)
            crop = img[y1:y2, x1:x2]
            croppath = os.path.join(path_train,name)
            cv2.imwrite(croppath,crop)

GenTrain()