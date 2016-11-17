import cv
import os

def Zoom(image,m,n):
    H = int(image.height*m)
    W = int(image.width*n)
    size = (W,H)
    zoom = cv.CreateImage(size,image.depth,image.nChannels)
    for i in range(H):
        for j in range(W):
            x1 = int(i/m)
            x2 = int((i+1)/m)
            y1 = int(j/n)
            y2 = int((j+1)/n)
            sum = [0,0,0]
            for k in range(x1,x2):
                for l in range(y1,y2):
                    sum[0] = sum[0]+image[k,l][0]
                    sum[1] = sum[1]+image[k,l][1]
                    sum[2] = sum[2]+image[k,l][2]
            num = (x2-x1)*(y2-y1)
            zoom[i,j] = (sum[0]/num,sum[1]/num,sum[2]/num)
    return zoom
path = '/home/lxy/ears/test/'
newpath = '/home/lxy/ears/finish/'
list = os.listdir(path)
for name in list:
    image = cv.LoadImage(path + name,1)
    zoom1 = Zoom(image,0.2,0.2)
    #cv.ShowImage('image',image)
    #cv.ShowImage('zoom',zoom1)
    cv.SaveImage(newpath + name , zoom1)
    #cv.WaitKey(0)

