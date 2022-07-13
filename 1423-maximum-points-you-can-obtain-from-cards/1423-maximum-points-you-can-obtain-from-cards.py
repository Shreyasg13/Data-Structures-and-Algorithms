class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         l=len(cardPoints)
        
#         if len(cardPoints)==k:
#             return sum(cardPoints)
        
#         if cardPoints[0] > cardPoints[-1]:
#             return cardPoints[0] + max(sum(cardPoints[1:k]),sum(cardPoints[l-k+1:l+1]))
#         elif cardPoints[0] < cardPoints[-1]:
#             return cardPoints[-1]+ max(sum(cardPoints[0:k-1]),sum(cardPoints[l-k:l]))
#         else:
#             return max(sum(cardPoints[0:k]),sum(cardPoints[l-k:l+1]))
        
#         class Solution:
    def maxScore(self, C: List[int], K: int) -> int:
        best = total = sum(C[:K])
        for i in range (K-1, -1, -1):
            total += C[i + len(C) - K] - C[i]
            best = max(best, total)
        return best
        
        
        