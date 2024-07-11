#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 21:38:42 2022

@author: murat
"""


def max_product_from_cut_pieces(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    
    
    
    table=[0]*(n+1)
    
    
    table[1]=1
    table[2]=1
    
    
    for i in range(2,n+1):
        for c in range(1,i):
          table[i]=max(table[i-c]*table[c],table[i-c]*c,(i-c)*c,table[i])
        print('table_',i,',:',table[i])
    
    
    return table[n]

print(max_product_from_cut_pieces(10))