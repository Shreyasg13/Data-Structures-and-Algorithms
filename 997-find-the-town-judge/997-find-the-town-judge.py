class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted=[0]*(n+1)
        
        for x,y in trust:
            trusted[x]-=1
            trusted[y]+=1
        for i in range(1,n+1):
            if trusted[i]==n-1:
                return i
        return -1
 