class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1,c1,r2,c2 =0,0,len(matrix)-1,len(matrix[0])-1
        
        while r1 <= r2 :
            In_row=(r1+r2)//2
          # Selecting a row  
            if matrix[In_row][0] > target : #checking first elemnt of middle row
                r2=In_row -1
            elif matrix[In_row][-1] < target : #checking last ele of middle row
                r1=In_row + 1
            else:
                break
        if not(r1 <= r2):
            return False
        
        # searching for a value in column
        
        while c1 <= c2 :
            mid=(c1+c2)//2
            if target > matrix[In_row][mid] :
                c1=mid+1
            elif target < matrix[In_row][mid]:
                c2=mid-1
            else:
                return True
        return False
                
            