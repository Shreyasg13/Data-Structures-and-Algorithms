class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # 1. Create Map
        map={c :i for i,c in enumerate(order)}
        """
        # Map 2
        map={}
        for val,key in enumerate(order):
            map[key]=val
        print(map)
        """
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                
                if j >= len(words[i+1]):
                    return False
                
                if words[i][j] != words[i+1][j]:
                    if map[words[i][j]] > map[words[i+1][j]] :
                        return False
                    break
        return True
                
            
      