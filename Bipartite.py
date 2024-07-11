
def isBipartite(graph):
    
    visited=[-1]*len(graph)
    
    subgroup=[-1]*len(graph)
    
    for i in range(len(graph)):
        if visited[i]==-1:
            subgroup[i]=0
            
            if DFS(i,visited,subgroup,graph) is False:
                return False
            
    return True   
        
def DFS(node,visit,color,adj):  
    visit[node]=1
    
    for w in adj[node]:
        if visit[w]==-1:
            
            color[w]=1-color[node]
            if DFS(w,visit,color,adj) is False:
                return False
        else:
            if color[w]!=color[node]:
             continue
            else:
             return False
       
    return True












graph1 = [[1,2],[0],[0]]
print(isBipartite(graph1))