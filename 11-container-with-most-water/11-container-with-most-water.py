class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        Maxarea=0
        while(l<r):
            
            area=min(height[l],height[r])*(r-l)
            Maxarea=max(Maxarea,area)
            # print(height[l],height[r],l,r,area)
            
            if height[l] >= height[r] :
                r-=1
            elif height[l] <= height[r] :
                l+=1
            
            
        return Maxarea
                            