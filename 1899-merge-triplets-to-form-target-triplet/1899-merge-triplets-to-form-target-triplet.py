class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_triplet = [1, 1, 1]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                max_triplet[0] = max(max_triplet[0], triplet[0])
                max_triplet[1] = max(max_triplet[1], triplet[1])
                max_triplet[2] =max(max_triplet[2], triplet[2])
            if max_triplet == target:
                return True
        return False
            
            
                
        
#         if target in triplets:
#             return True
        
#         def operation(a,b):
#             ans=[]
#             for i in range(len(triplets[0])):
                
#                 ans.append(max(a[i],b[i])) 
#             return ans

#         val=[] 
#         for i in range(len(triplets)):
#             for j in range(len(triplets),i+1):
#                 val=operation(triplets[i],triplets[j])
#                 if val == target:
#                     return True
                
#             top=triplets.pop()
#             triplets.append(val)
            
#         return False
                    
                    
    
                
                
                
            
        
       