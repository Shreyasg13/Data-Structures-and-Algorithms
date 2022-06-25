class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map=defaultdict(list)
        
        for word in strs:
            hash=[0]*26
            for c in word:
                hash[ord(c)-ord('a')]+=1
            Map[tuple(hash)].append(word)
            
        # print(Map.keys(),"\n")
        # print(Map.values())
        return Map.values()