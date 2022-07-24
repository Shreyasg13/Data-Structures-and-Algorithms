class Solution:
	def Found(self, nums, target):
		# if len(nums) == 1 and nums[0] == target:
		# 	return 0
		if len(nums) == 1 and nums[0] != target:
			return -1
    
		l,r = 0,len(nums)-1
		
		while l <= r:
			m = (l + r)//2
			if nums[m] == target:
				return m
			elif nums[m] > target:
				r = m-1
			else:
				l = m+1
		return (-1)

	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		row = len(matrix)
        # Searching element in each row
		for i in range(row):
            # if target not found
			if self.Found(matrix[i], target) == -1:
				continue
			else:
				break
 
		if self.Found(matrix[i], target) != -1:
			return True
		return False