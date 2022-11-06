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
        # 2. compare two words character by character
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                # for case like apple and app
                if j >= len(words[i+1]):
                    return False
                # check if they are sorted if not equal
                if words[i][j] != words[i+1][j]:
                    if map[words[i][j]] > map[words[i+1][j]] :
                        return False
                    break
        return True
                
            
      