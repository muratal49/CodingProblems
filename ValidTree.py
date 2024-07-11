def is_it_a_tree(n, edge_start, edge_end):
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
    for i,src in enumerate(edge_start):
          adj_list[src].append(edge_end[i])
          adj_list[edge_end[i]].append(src)
        
    visited=[-1]*n
    
    connected=0
    nodes=0
    
    parent=[-1]*n
   
   
    
            
    for i in range(n):
        
        if len(adj_list[i])==0:
            return False
            
        if visited[i]==-1:
            
            if DFS(i,visited,adj_list,parent) is False:
               return False
            
            connected+=1
            
        if connected>2:
            return False

   
    return True


def DFS(node,visit,adj,par):
    visit[node]=1
    #nodess+=1
    for neighbor in adj[node]:
       if visit[neighbor] == -1:
           par[neighbor]=node
           DFS(neighbor,visit,adj,par)
       else:
           if par[node] !=  neighbor:
                return False
        
        

    return True
    