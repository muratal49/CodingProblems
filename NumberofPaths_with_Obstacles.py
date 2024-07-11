#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 22:45:15 2022

@author: murat
"""

def number_of_paths(g):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    
    n=len(g)
    m=len(g[0])
    
   
    table=[[0]*(m) for row in range(n)]
  
    
    if g[0][0]==0:
        return 0
    else:
        table[0][0]=1
    
    print(table)
        
    for i in range(1,n):
        if g[i][0] != 0:
            
            table[i][0]=1
        else:
            break
    
    for j in range(1,m):
        if g[0][j] != 0:
             table[0][j]=1
        else:
            break
    
    for i in range(1,n):
        for j in range(1,m):
            if g[i][j] != 0:
                table[i][j]=table[i-1][j]+table[i][j-1]
    
    
    
    
    print(table)
    return table[n-1][m-1]

g=[
[1, 1, 1, 1],
[1, 1, 1, 1],
[1, 1, 1, 1]
]

print(number_of_paths(g))
