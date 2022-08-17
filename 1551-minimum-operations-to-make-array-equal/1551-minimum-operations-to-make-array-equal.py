class Solution:
    def minOperations(self, n: int) -> int:
        # n=5
        # 1 3 5 7 9 11 even case
        # 1 3 5 7 9 odd case
        
        arr=[0]*n
        for i in range(n):
            arr[i]= (2 * i) + 1
        
          
        res,mid_val=0,0
        
        if n%2==0:
            
            
            mid=n//2
            mid_val=(arr[mid]+arr[mid-1])//2
            for i in range(n//2):
                print(i)
                res+=mid_val-arr[i]
                
        else:
            
            mid_val=n//2 
            for i in range(n//2):
                res+=( arr[mid_val]-arr[i])
        return res
                
                
                
            
            
            
            
        
        
        
        