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

video_name = "Duke Game 1 Center Field.mp4"

vidObj = cv2.VideoCapture(video_name)

count = 1;

start = time.time()

while count <= 150:
    
    # Image dimensions: (720, 1280)
    success, image = vidObj.read()
    #image = image[:,int(1280/4): int(1280*3/4)]
    
    #if (count == 1):
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("frames/frame{:05d}.jpg".format(count), image)
    
    count += 1;
    
end = time.time()
time_taken = end - start

print("Time taken for " + str(count-1) + " frames: " + str(time_taken))
