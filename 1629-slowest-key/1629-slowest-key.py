class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_index=0
        cur_time=releaseTimes[0]
        for i in range(1,len(releaseTimes)):
            print(releaseTimes[i])
            new_time=releaseTimes[i]-releaseTimes[i-1]
            if  new_time > cur_time  :
                max_index=i
                cur_time=max(cur_time,new_time)
                
            if (cur_time == new_time and ord(keysPressed[i]) >  ord(keysPressed[max_index]) ):
                max_index=i
                
        return keysPressed[max_index]
                
            
        
        