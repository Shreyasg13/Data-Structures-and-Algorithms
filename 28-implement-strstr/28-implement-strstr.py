class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        gap=len(needle)
        for i in range(len(haystack)-gap+1):
            word=haystack[i:i+gap]
            if word==needle:
                return i
        return -1
        
        