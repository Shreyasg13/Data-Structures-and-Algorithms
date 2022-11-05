class Solution:
    def maxLength(self, arr: List[str]) -> int:
        DP=[""]
        res=0
        
        for word in arr:
            
            for i in range(len(DP)):
                
                tmp=DP[i] + word
                
                if len(tmp)!=len(set(tmp)):
                    continue
                    
                DP.append(tmp)
                res=max(res,len(tmp))
        return res
        
        
#     # arr = ["un","iq","ue","ue"]
        
#         c=a+b
#         bag=set()
#         for ch in c:
#             if ch not in bag:
#                 bag.add(ch)
#             else:
#                 return False
#         return True        
        
#     def maxLength(self, arr: List[str]) -> int:
#         i=0
#         max_len=0
#         while i < len (arr):
#             if len(arr[i])!=len(set(arr[i])):
#                 i+=1
#                 continue
                
#             cur=arr[i]
            
#             for j in range(len(arr)):
#                 if len(arr[j])!=len(set(arr[j])):
#                     continue
#                 if self.isUnique(cur,arr[j]) and i != j :
#                     cur+=arr[i]
#             max_len=max(max_len,len(cur))
            
#             i+=1
    
#         return max_len
                
        
        
       
            
        
        