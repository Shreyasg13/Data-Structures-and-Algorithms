class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Bruteforce approach O(n^2) TLE
        # res=[]
        # for i in range(len(arr)-1):
        #     cur_max=float('-inf')
        #     for j in range(i+1,len(arr)):
        #         cur_max=max(cur_max,arr[j])
        #     res.append(cur_max)
        # res.append(-1)
        # return res
        
        right_max=-1
        
        for i in range(len(arr)-1,-1,-1):
            cur_max=max(right_max,arr[i])
            arr[i]=right_max
            right_max=cur_max
        return arr