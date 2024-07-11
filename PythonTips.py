#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 12:33:59 2022

@author: murat
"""


# inline For loops for set or lists
a=['abc','def','cciq']

b=[[c] for words in a for c in words]  #a list
k={c:set() for words in a for c in words}  # a dictionary ofsets


# Initiazing an array inline loop

new=[[1]*10 for i in range(3)]

for i,node in enumerate(k):
    r.append(list(k[node]))
 
    
#initilaizing 2D array given the size of a 2D matrix entry
new=[[0]*cols for i in range(rows)]