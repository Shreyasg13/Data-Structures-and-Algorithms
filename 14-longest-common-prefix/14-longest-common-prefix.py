class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=strs[0]
        for word in strs:
            while(common!=word[0:len(common)]):
                common = common[0:(len(common)-1)]
        return common