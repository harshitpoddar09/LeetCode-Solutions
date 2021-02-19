#Submission 1 (faster)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
    
#Submission 2
class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]
