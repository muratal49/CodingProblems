#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 08:45:51 2022

@author: murat
"""

def SumSetlist(A,t):
    
    def patt(idx,partial_solution): 
        
        if sum(partial_solution)==t:
            print(partial_solution)
            return True
        
            #return 
        
        if len(A)==idx:
            
          # print(partial_solution)
            return 
        #recurison
        
        patt(idx+1,partial_solution) 
        #include:
        partial_solution.append(A[idx])
        patt(idx+1,partial_solution) 
        partial_solution.pop()  
        
    patt(0,[])
    
# the bactraking prunes the branch after it finds the sum, 1 and does not need to go down to 1, 0 pair.
#so if you have 0 after 1 in the list, it will not appear in the result.
SumSetlist([2,0], 2)
