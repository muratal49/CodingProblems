def main(A:list[int]):
    def patt(idx,partial_solution): 
        if len(A)==idx:
           print(partial_solution)
           return 
        #recurison
        
        patt(idx+1,partial_solution) 
        #include:
        partial_solution.append(A[idx])
        patt(idx+1,partial_solution) 
        partial_solution.pop()  
          
    patt(0,[])  
    

main([1,2,3])