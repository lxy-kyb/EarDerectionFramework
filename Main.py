# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import os
import sys
import cvimgshow
import cvimgimprove
import SelectiveSearch as ss
import ZoomCV
import time

class FrameworkMain(QtGui.QWidget):
    def __init__(self):
        super(FrameworkMain, self).__init__()
        self.initUI()

    def initUI(self):
        self.img = None
        self.hbox = QtGui.QHBoxLayout()
        self.btn_LoadImage = QtGui.QPushButton('Load', self)
        self.btn_LoadImage.clicked.connect(self.LoadImage)

        self.btn_ToGrayScale = QtGui.QPushButton('ToGaryScale', self)
        self.btn_ToGrayScale.clicked.connect(self.ToGrayScale)

        self.btn_ImproveImage = QtGui.QPushButton('Improve', self)
        self.btn_ImproveImage.clicked.connect(self.ImproveImage)

        self.btn_ScaleNormalization = QtGui.QPushButton('ScaleNormailzation', self)
        self.btn_ScaleNormalization.clicked.connect(self.ScaleNormalization)
                
        self.hbox.addWidget(self.btn_LoadImage)
        self.hbox.addWidget(self.btn_ScaleNormalization)
        self.hbox.addWidget(self.btn_ToGrayScale)
        self.hbox.addWidget(self.btn_ImproveImage)        
        self.hbox.addStretch()

        self.h2box = QtGui.QHBoxLayout()
        self.btn_SelectiveSearch = QtGui.QPushButton('SelectiveSearch', self)
        self.btn_SelectiveSearch.clicked.connect(self.SelectiveSearch)

        self.h2box.addWidget(self.btn_SelectiveSearch)
        self.h2box.addStretch()

        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.h2box)
        self.vbox.addStretch()

        self.setLayout(self.vbox)
        self.show()

    def LoadImage(self):
        fileDialog = QtGui.QFileDialog.getOpenFileName(self, 'Path', os.getcwd(), 'Images (*.png *.jpg)')
        if fileDialog != '':
            self.img = cvimgshow.GetImg(str(fileDialog))
            cvimgshow.showImg('Source IMG', self.img)
    
    def ImproveImage(self):
        if self.img is not None:
            gray = cvimgshow.ToGrayScale(self.img)
            i = cvimgimprove.improve(gray)
            cvimgshow.showImg('Improve', i)

    def ToGrayScale(self):
        if self.img is not None:
            gray = cvimgshow.ToGrayScale(self.img)
            cvimgshow.showImg('GrayScale',gray)           
            
    def SelectiveSearch(self):
        if self.img is not None:           
            for i in range(0,300):
                self.img = ss.RamdomRect(self.img)                               
                cvimgshow.showImg('Selective Search', self.img)               

    def ScaleNormalization(self):
        if self.img is not None:
            self.img = ZoomCV.Scale(self.img, 896,672)
            cvimgshow.showImg('ScaleNormalization', self.img)

def main():
    app = QtGui.QApplication(sys.argv)
    fm = FrameworkMain()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
       