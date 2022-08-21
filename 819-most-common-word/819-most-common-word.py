class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq={}
        spe_char=("!?',;.")
        sp=' '   
        max_freq,i=0,0
       
        while len(paragraph) > i:
            print(i)
            
             
            # creating a valid word   
            word=""
            while 'a'<= paragraph[i].lower() <= 'z' and i < len(paragraph): 
                
                word+=paragraph[i].lower()
                i+=1
                if i==len(paragraph):
                    break
            i+=1        
                
            
            if word != sp and word not in banned and word not in spe_char:
                if word not in freq:    
                    freq[word]=1
                else:
                    freq[word]+=1
                
                
            
                if freq[word] > max_freq:
                    max_freq=freq[word]
                    MCW=word
            print(freq)   
        return MCW
            
         
        
        
            
            
            
            
            
        