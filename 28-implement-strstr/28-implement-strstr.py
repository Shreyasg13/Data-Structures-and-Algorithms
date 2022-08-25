class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        if not needle:
            return 0
        for i in range(len(haystack)-k+1):
            word=haystack[i:i+k]
            print(word)
            if word==needle:
                return i
        return -1
        
        