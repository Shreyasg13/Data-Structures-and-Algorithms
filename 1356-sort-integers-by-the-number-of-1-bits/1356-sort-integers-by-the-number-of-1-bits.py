class Solution:
    def sortByBits(self, array: List[int]) -> List[int]:
        def helper(d):
            count=0
            d = str(bin(d))
            for n in d:
                if n=="1":
                    count+=1
            return count
        return sorted(array, key=lambda x: (helper(x), x))