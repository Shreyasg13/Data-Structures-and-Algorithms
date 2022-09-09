class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals=sorted(intervals,key=lambda x:x[0])
        
        stack=[]
        
        for i in range(len(intervals)):
            if stack and stack[-1][1] >= intervals[i][0]:
                stack[-1][1]=max(stack[-1][1],intervals[i][1])
                continue
                
            stack.append(intervals[i])
        return stack
                

