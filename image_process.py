#!/usr/bin/env python
#coding=utf-8
import os
import sys
import numpy as np
import cv2

def improve(inpath,outpath):
    img = cv2.imread(inpath,0)
    clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    cl2 = clahe.apply(cl1)
    name = inpath.split("/")[-1]
    newpath = outpath + '/' + name
    cv2.imwrite(newpath,cl2)
    print newpath




def listpuredir(dirsource,dirdes):
	
	
	index=0
	filenum=0
	list=os.listdir(dirsource)
	for line in list:
		filepath = os.path.join(dirsource,line)
		if os.path.isdir(filepath):#如果filepath是目录，则再列出该目录下的所有文件
			pass
		else:
			print filepath
			improve(filepath,dirdes)
			


checkdir="EarLib"
desdir="Ne"
listpuredir(checkdir,desdir)

raw_input("\r\n Press any key to exit.")

