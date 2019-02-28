#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:15:39 2019

@author: jeetu
"""

import pandas as pd

df = pd.read_csv("demo.txt", sep = " ", header=None , names=['a','b','c',] )
print (df)

dataset= pd.read_csv("demo.txt", delimiter="\t")
print(dataset) 
dataset.head(10)
