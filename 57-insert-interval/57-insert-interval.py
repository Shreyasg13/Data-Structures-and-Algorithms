class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack=[]
        intervals.append(newInterval)
        intervals=sorted(intervals,key=lambda x :x[0])
        
        for i in range(len(intervals)):
            if stack and stack[-1][1] >= intervals[i][0]:
                stack[-1][1]=max(stack[-1][1],intervals[i][1])
                continue
            stack.append(intervals[i])
            
        return stack
            
        
        
        
#             if intervals[i][0] > newInterval[1] :
#                 stack.append(newInterval)
#                 return stack + intervals[i:]
#             elif intervals[i][1] < newInterval[0]:
#                 stack.append(intervals[i])
#             else:
#                 temp=[min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]
#                 stack.append(temp)
                
#         return stack
