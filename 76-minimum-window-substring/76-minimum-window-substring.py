class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        window,target={},{}
        
        for c in t:
            target[c]=1+target.get(c,0)
        
        have,need=0,len(target)
        res,reslen=[-1,-1],float("infinity")
        l=0
            
        for r in range (len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            
            #if element found increment have
            if c in target and target[c]==window[c]:
                have+=1
                
            while have==need:
                # serching for min window
                if (r-l+1) < reslen:
                    res=[l,r]
                    reslen=(r-l+1)
                    
                window[s[l]]-=1
                if s[l] in target and target[s[l]] > window[s[l]]:
                    have-=1
    
                l+=1
        
        l,r=res
        
        return s[l:r+1] if reslen!=float("infinity") else ""
            
    
       