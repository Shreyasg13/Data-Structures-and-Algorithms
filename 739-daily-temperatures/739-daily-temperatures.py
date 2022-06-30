class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # print(temperatures)
        ans=[0]*len(temperatures)
        stack=[]
        
        for i,val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                cur=stack.pop()
                ans[cur]=i-cur
            stack.append(i)
            
        return ans
                
#         for i in range(len(temperatures)):
#             for j in range(i+1,len(temperatures)):
#                 if temperatures[i]< temperatures[j]:
#                     ans[i]=j-i
#                     break
        
#         return ans
            
            

        