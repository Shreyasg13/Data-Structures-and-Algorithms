class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n==0: return -1
        Map=defaultdict(set)
        
        for i in range(1,n+1):
            Map[i] = set()
        
        for x,y in trust:
            Map[x].add(y)
        
        # person having no edges  
        
        person = [i for i,v in Map.items() if len(v) == 0]
        
        if len(person) == 0: return -1
        person = person[0]
        
        # go through edges and see if everybody trusts candidate
        for i,v in Map.items():
            
            if person == i: continue
            if person not in Map[i]:
                return -1
        return person