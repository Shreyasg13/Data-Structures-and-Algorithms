class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse=True)
        
        sz = 0
        mxUnits = 0
        
        for size, units in boxTypes:
            if sz+size < truckSize:
                sz += size
                mxUnits += size*units
            else:
                mxUnits += (truckSize-sz)*units
                break
        
        return mxUnits
                
 