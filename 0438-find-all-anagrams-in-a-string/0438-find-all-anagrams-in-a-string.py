class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 1. Early answer based on p2s length
        if len(s) < len(p):
            return []
        hash_s,hash_p={},{}
        # 2. create two hashmaps of length p
        for i in range(len(p)):
            hash_s[s[i]] = 1 + hash_s.get(s[i],0)
            hash_p[p[i]] = 1 + hash_p.get(p[i],0)
        # 3. declaring res 
        res=[0] if hash_s==hash_p else []
        
        """
        # 4. Sliding Window starting from index : l to r 
        maintining/Updating window hash values in hash_s
        """ 
        l=0
        for r in range(len(p),len(s)):
            hash_s[s[l]]-=1
            hash_s[s[r]]= 1 + hash_s.get(s[r],0)
            """
            a. after removing leftmost char if hashvalue becomes zero
            i.e. char does'nt exist in window, pop char from hashmap
            """
            if hash_s[s[l]]==0:
                hash_s.pop(s[l])
            l+=1
            """
            b. if both hashmaps are equal, i.e. cur str is anagram,so store an index
            """ 
            if hash_s==hash_p:
                res.append(l)
        
        return res
            