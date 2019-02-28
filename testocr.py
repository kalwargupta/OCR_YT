#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Wed Nov 28 12:33:08 2018

@author: jordansauchuk
'''


from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
'''


with Img(filename='ai-handbook.pdf', resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='image_name_example.jpg')

demo = Image.open("image_name_example-1.jpg")
text = pytesseract.image_to_string(demo, lang = 'eng')
print(text)


example = text

def  prepreocess(sent):
    sent  = nltk.word_tokenize(sent)
    sent = nltk.pos_sent(sent)
    return sent

sent = preprocess(example)
print(sent)

'''



demo = Image.open("receipt.png")
text = pytesseract.image_to_string(demo, lang = 'eng')

with open('demo.txt', 'a') as f:
    print(text, file=f)


if'320918380' in open('demo.txt').read():
    print("True")
    
#pip install goslate
import goslate
gs = goslate.Goslate()
print(gs.translate(text, 'de'))


