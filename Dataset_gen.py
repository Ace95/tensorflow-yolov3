#######################################################################
#### Author: Marco Acerbis, 4Solid s.r.l. #############################
#### Copyright (C) 2019 * Ltd. All rights reserved. ###################
#### File: Dataset_gen.py ############################################
#### Date: 27/03/19 ###################################################
#### Editor: Visual Studio Code #######################################
#######################################################################

import cv2
import numpy as np
import io

file = open("dataset.txt",'a')

# CALLBACK FUNCTION
drawing = False # True if mouse is pressed
ix,iy = -1,-1

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        # When you click DOWN with left mouse button drawing is set to True
        drawing = True
        # Then we take note of where that mouse was located
        ix,iy = x,y

    elif event == cv2.EVENT_LBUTTONUP:
        # Once you lift the mouse button, drawing is False
        drawing = False
        # we complete the rectangle.
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),3)
        line = [" ",str(ix)," ",str(iy)," ",str(x)," ",str(y)," ","0"]
        file.writelines(line)

""" # GENERATE THE FILELIST
file2 = open("filelist.txt","a")
for i in range(1,201):

    line = ["\n","./dog_dataset/images/dog.",str(i),".jpg"]
    file2.writelines(line)

file2.close() """

f = open("./filelist.txt")
  
lines = [line.rstrip('\n') for line in f.readlines()]


for path in lines:
    
    # This names the window so we can reference it 
    cv2.namedWindow(winname='dog')

    # Connects the mouse button to our callback function
    cv2.setMouseCallback('dog',draw_rectangle)

    img = cv2.imread(path)
    line = ["\n",path]
    file.writelines(line)

    while True: 

        # Shows the image window
        cv2.imshow('dog',img)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
  
  
file.close()
