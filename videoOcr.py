#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 11:29:20 2019

@author: jeetu
"""

from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy

import os
import cv2
'''
if not os.path.exists('image_frames'):
    os.makedirs('image_frames')

#creating the video path 

test_vid= cv2.VideoCapture('testvideo.mp4')

index=

while test_vid.isOpened():
    ret,frame=test_vid.read()
    if not ret:
        break

    #assign name for files
    name="./image_frames/frame"+str(index)+".png"
    
    #assign print statement

    cv2.imwrite(name, frame)
    print("Extracting frames......."+name)
    index+=1
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    
test_vid.release()
cv2.destroyAllWindows()
'''


demo=Image.open("./image_frames/frame115.png")
text=pytesseract.image_to_string(demo, lang="eng")
print(text)
    