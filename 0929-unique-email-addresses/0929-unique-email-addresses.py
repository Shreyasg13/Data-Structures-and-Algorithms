class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        
        # function to filter local name
        def filter(str):
            res=""
            for c in str:
                if c =='+':
                    break
                if c != '.':
                    res+=c
            return res
        
        container=set()
        
        # reform each mail and append it in an container
        for email in emails:
            
            x=email.split('@')
            local_name=filter(x[0])
            domain_name=x[1]
            
            
            obj=local_name+'@'+domain_name
            print(obj)
            if obj not in container:
                container.add(obj)
        return len(container)
                
            
            
            
        
        
        
        