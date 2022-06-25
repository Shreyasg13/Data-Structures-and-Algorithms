class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map=defaultdict(list)  
        for word in strs:
            Map[tuple(sorted(word))].append(word)     
        return Map.values()
