class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2==1:
            return []
        
        count=Counter(changed)
        res=[]
        
        for num in sorted(changed):
            doubled=num*2
            if count.get(doubled,0) > 0 and count.get(num,0) > 0:
                res.append(num)
                count[num]-=1
                count[doubled]-=1
            elif num//2 not in count or num%2==1:
                return []
            
        return res