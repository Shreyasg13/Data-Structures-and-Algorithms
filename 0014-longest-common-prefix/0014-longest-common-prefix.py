class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # keep on eliminating each ending character if it not common among all
        pre=strs[0]
        for word in strs:
            # keep on shorting the prefix till it doest mach the prefix
            while(pre!=word[0:len(pre)]):
                pre = pre[0:(len(pre)-1)]
        return pre