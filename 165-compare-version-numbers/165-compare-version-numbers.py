class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        l1,l2,=len(nums1),len(nums2)
        
        for i in range(max(l1,l2)):
            d1=int(nums1[i]) if i < l1 else 0
            d2=int(nums2[i]) if i < l2 else 0 
            
            if d1 > d2:
                return 1
            elif d1 < d2:
                return -1
        return 0
        
       
                
                   
            
          