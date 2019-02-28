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

'''
# Should run only 1 time for generating images from pdf file as per pages

with Img(filename="ai-handbook.pdf", resolution=300) as img:
    img.compression_quality=99
    img.save(filename="image_name_example.jpg")



demo=Image.open("questionpapaer.jpg")
text = pytesseract.image_to_string(demo, lang="eng")
print (text) 

example_text=text

def preproccess(sent):
    sent =word_tokenize(sent)
    sent = pos_tag(sent)
    return sent

sent = preproccess(example_text)

print (sent) 
'''



demo=Image.open("receipt.png")
text = pytesseract.image_to_string(demo, lang="eng")
print (text) 

with open ("demo.txt","a")as f:
    print (text, file=f)

if "320918380" in open("demo.txt").read():
    print ("true")