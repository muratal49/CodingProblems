#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:04:57 2022

@author: murat
"""

def helper(idx,partial_solution,A,s): 
    
    if len(A)==idx:
           #print(partial_solution,type(partial_solution))
           s+=[partial_solution]
          
           return 
      #subsets
        #recurison
        
    helper(idx+1,partial_solution,A,s) 
    #include:
    t=partial_solution
    partial_solution=partial_solution+A[idx]
    helper(idx+1,partial_solution,A,s) 
    partial_solution=t
    return  
  

def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    subsets=[]
    helper(0,"",s,subsets) 
    return  print(subsets)
 
generate_all_subsets('123')