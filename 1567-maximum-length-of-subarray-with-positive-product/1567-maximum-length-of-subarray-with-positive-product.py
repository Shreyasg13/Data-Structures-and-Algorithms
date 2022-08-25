class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len=pos=neg=0
        
        for n in nums:
            
            # if n is +ve and if pos prod len increment by 1 and
            # negetive product len also increment by one
            if n > 0:
                pos=pos+1
                neg=neg+1 if neg else 0
            
            # if n is -ve and if pos prod will obtain by neg prod so, we add neg product len
            # on the other side neg prod len incremnet with pos product len +1 
            elif n < 0:
                pos,neg=neg+1 if neg else 0,pos+1
            
            else:
                pos=neg=0
                
            max_len=max(max_len,pos)
        return max_len
        