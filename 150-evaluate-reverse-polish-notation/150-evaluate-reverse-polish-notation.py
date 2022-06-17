class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations=['+','-','*','/']
        stack=[]
        
        for num in tokens:
           
            if num not in operations:
                stack.append(int(num))
            else:
                # print(stack)
                
    
                if num=='+' : 
                    n1=stack.pop()
                    n2=stack.pop()
                    stack.append(n1+n2)
                if num=='-' : 
                    n1=stack.pop()
                    n2=stack.pop()
                    stack.append(n2-n1)
                if num=='*' : 
                    n1=stack.pop()
                    n2=stack.pop()
                    stack.append(n1*n2)
                if num=='/' : 
                    
                   
                    n1=stack.pop()
                    # print(stack)
                    n2=stack.pop()
                    
                   
                    stack.append(int(n2/n1))
                
                    
        return stack[-1]
        