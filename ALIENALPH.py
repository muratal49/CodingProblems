#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 16:36:41 2022

@author: murat
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 08:37:10 2022

@author: murat
"""

def AlienAlphabet(Wordlist):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # Write your code here.
    
    Adj_list={c:set() for words in Wordlist for c in words}
    
    for i in range(len(Wordlist)-1):
        w1,w2= Wordlist[i],Wordlist[i+1]
        for k in range(min(len(w1),len(w2))):
            if w1!=w2:
            
              Adj_list[w1[k]].add(w2[k])
              break
          #you should also consider the case like abcd abc which is not 
          #possible, not correct so exit and return none
    adj=list(Adj_list.values())          
             
    visited=[-1]*len(Adj_list)
    dep=[-1]*len(Adj_list) # I will check for Departures, if not updated then
    #it is still in the call stack
    toplist=[]*len(Adj_list)
               
    for i in range(len(Adj_list)):
           
           if visited[i]==-1:
               
               if DFS(i,visited,Adj_list,dep,toplist) is False:
                  return False
            
               

    print("the Dictionary:", Adj_list) 
    print('visited array=',visited)
    print(toplist)
    return toplist


def DFS(node,visit,adj,depar,top):
       visit[node]=1
       for k,neighbor in enumerate(adj[node]):
         if visit[k] == -1:
              
           if DFS(k,visit,adj,depar,top) is False:
              return False
         else:
              if depar[node]==-1:
                  return False
              
       depar[node]=1
       top.append(adj[node])

       return top     
   
    

W=['wrt','wrf','er','ett','rftt']

AlienAlphabet(W)

