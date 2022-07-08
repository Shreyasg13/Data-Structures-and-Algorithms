class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res=[] 
        self.dfs(s,[],res)
        return res
# DFS For going throught each path
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
            return 
        for i in range(1,len(s)+1):
# check if the string is pallindrome and then recursively call dfs on the remaining string
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:],path+[s[:i]],res)
# Function to check if the sting is pallindrome or not
    def isPalindrome(self,s):
        return s==s[::-1]
        
        