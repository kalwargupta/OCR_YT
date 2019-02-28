#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:10:22 2019

@author: jeetu
"""

from PIL import Image
import pytesseract
from wand.image import Image as Img

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist



#Opening the image with PIL
demo_one=Image.open('example.png')
# converting to image to string with pytesseract 
text_one=pytesseract.image_to_string(demo_one, lang='eng')
#print the converted image to string data
print (text_one)

demo_two=Image.open('receipt.png')
text_two=pytesseract.image_to_string(demo_two, lang='eng')
print(text_two)

#tokenizing 

token_word_one = word_tokenize(text_one)
token_word_two = word_tokenize(text_two)

print (token_word_one)
print(token_word_two)

#Freqency Distribution
freq_dist_one = FreqDist(token_word_one)
freq_dist_two = FreqDist(token_word_two)


#plotting the freq dist to graph

import matplotlib.pyplot as plt

freq_dist_one.plot(30,cumulative=False)
freq_dist_two.plot(30)
