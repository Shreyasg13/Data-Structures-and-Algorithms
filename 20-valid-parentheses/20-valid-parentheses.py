class Solution:
    def isValid(self, s: str) -> bool:
        Map={ "}":"{",")":"(","]":"["}
        stack=[]
        
        for char in s:
            if char in Map:
                if stack and stack[-1]==Map[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return False if stack else True 
    
        