import queue
def count_islands(M):
    """
    Args:
     matrix(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    islands=2;
    rows=len(M)
    cols=len(M[0])
    new=[[0]*cols for i in range(rows)]
    for i in range(0,rows):
        for j in range(0,cols):
           if M[i][j]==1:
               islands+=1
               BFS(M,new,i,j,islands)
    return islands-2,new #, M
    
    
def BFS(A,B,ii,jj,counts):
    q=queue.Queue()
    q.put([ii,jj])

    while not q.empty():
        node=q.get()
        
        for ni,nc in getneighbors(A,node[0],node[1]):
            A[ni][nc]=counts
            B[ni][nc]=counts-2
            q.put([ni,nc])
            
        
    return
        




def getneighbors(A,row,col):
    
    rowss=len(A)
    colss=len(A[0])
    neighbor=[]
    #up
    if row>=1 and A[row-1][col]==1:
        neighbor.append([row-1,col])
        
       # A[row-1][col]=count
        
    #down
    if row<rowss-1 and A[row+1][col]==1:
        neighbor.append([row+1,col])
       # A[row+1][col]=count
    
    #left
    if col>=1 and A[row][col-1]==1:
        neighbor.append([row,col-1])
        #A[row][col-1]=count 
        
   #right
    if col<colss-1 and A[row][col+1]==1:
        neighbor.append([row,col+1])
         #A[row][col+1]=count
    
    #upright
    
    if row>=1 and col<colss-1 and A[row-1][col+1]==1:
        neighbor.append([row-1,col+1])
        #A[row-1][col+1]=count
    
    #upleft
    if row>=1 and col>=1 and A[row-1][col-1]==1:
        neighbor.append([row-1,col-1])
        #A[row-1][col-1]=count
    
    #downright
    if row+1<rowss and col+1<colss and A[row+1][col+1]==1:
        neighbor.append([row+1,col+1])
        #A[row+1][col+1]=count
    #downleft
    if row+1<rowss and col>=1 and A[row+1][col-1]==1:
        neighbor.append([row+1,col-1])
       # A[row+1][col-1]=count
    
    return neighbor

    
M=[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0]]