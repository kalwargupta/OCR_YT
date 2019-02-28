#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:45:07 2019

@author: jeetu
"""


from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy


demo= Image.open("image_name_example-5.jpg")
text=pytesseract.image_to_string(demo, lang="eng")
print(text)


image_file=Image.open("./image_frames/frame115.png")
image_file=image_file.convert('1')
image_file.save("BW.jpg")