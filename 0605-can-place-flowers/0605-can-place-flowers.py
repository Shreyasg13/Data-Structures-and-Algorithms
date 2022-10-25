class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        flowerbed=[0] + flowerbed + [0]
        count=0
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i+1]!=1 and flowerbed[i-1]!=1 :
                flowerbed[i]=1
                count+=1
                
        return count>=n
                
        
        