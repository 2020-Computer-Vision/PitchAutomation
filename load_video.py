#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:31:15 2019

@author: Jacob
"""

import numpy as np
import pandas as pd
import cv2
import time

#video_name = "UVA4-13-19Game2.mp4"
video_name = "Duke Game 1 3rd Base Dugout.mp4"

vidObj = cv2.VideoCapture(video_name)

count = 1;

start = time.time()

frames = {217,513,915,989,1223,1528,1546,1581,1856,1885,2315,2769,
            2793,2808,3123,3529,3547,3966,4250}

while count <= 4300:
    
    # Image dimensions: (720, 1280)
    success, image = vidObj.read()
    #image = image[:,int(1280/4): int(1280*3/4)]
    
    if (count in frames):
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("frames/frame{:05d}_pitchSIDE.jpg".format(count), image)
    
    count += 1;
    
end = time.time()
time_taken = end - start

print("Time taken for " + str(count-1) + " frames: " + str(time_taken))
