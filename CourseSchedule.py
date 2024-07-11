#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 08:37:10 2022

@author: murat
"""

def can_be_completed(n, a, b):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    adj_list=[[] for x in range(n)]
    for i in range(len(a)):
          adj_list[a[i]].append(b[i])
          
    visited=[-1]*n
    dep=[-1]*n  # I will check for Departures, if not updated then
    #it is still in the call stack
    
            
    for i in range(n):
        
        if visited[i]==-1:
            
            if DFS(i,visited,adj_list,dep) is False:
               return False
         
            

   
    return True


def DFS(node,visit,adj,depar):
    visit[node]=1
    
    for neighbor in adj[node]:
       if visit[neighbor] == -1:
           
           if DFS(neighbor,visit,adj,depar) is False:
               return False
       else:
           if depar[node]==-1:
               return False
           
       depar[node]=1

    return True
    