class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count_text=Counter(text)
        map_balloon=Counter("balloon")
        res=float("inf")
        for c in map_balloon:
            c_freq=count_text[c]//map_balloon[c]
            res=min(res,c_freq)
            
        return res
            
        