

def StringSub(A):
    def helper(idx,partial_solution): 
        if len(A)==idx:
           print(partial_solution)
           return 
        #recurison
        
        helper(idx+1,partial_solution) 
        #include:
        t=partial_solution
        partial_solution=partial_solution+A[idx]
        helper(idx+1,partial_solution) 
        partial_solution=t
          
    helper(0,"")  
    

StringSub('abc')