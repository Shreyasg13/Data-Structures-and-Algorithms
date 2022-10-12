class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        res.append([1])
        i=0
        
        while i < numRows-1 :
            # initial border 1
            layer=[1]
            # addition of in between values
            for j in range(1,len(res[i])):
                layer.append(res[i][j]+res[i][j-1])
            
            # end border 1
            layer.append(1)
            res.append(layer)
            i+=1
        return res
                
                
        