class Solution:
    def sortByBits(self, array: List[int]) -> List[int]:
        # helping function to calculate number of ones
        def Weight(d):
            count=0
            d = str(bin(d))
            for n in d:
                if n=="1":
                    count+=1
            return count
        # sort an array by the weight on ones i.e. key
        return sorted(array, key=lambda x: (Weight(x), x))