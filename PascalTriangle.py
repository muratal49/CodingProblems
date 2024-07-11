#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:17:09 2022

@author: murat
"""
def pyr(n):

    
    table=[[1 for col in range(0,row+1)]  for row in range(n)]
    print(table[0])
    print(table[1])
    for row in range(2,n):
        for col in range(1,row):
            table[row][col]=table[row-1][col-1]+table[row-1][col]
        print(table[row])
    
   
    return table


x=pyr(10)
