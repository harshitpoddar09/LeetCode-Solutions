#Submission2- 32ms
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            minimum=min(minimum,nums[i])
        return max(1-minimum,1)
        
#Submission1- 44ms
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum=nums[0]
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            minimum=min(minimum,nums[i])
        if minimum>=1:
            return 1
        return 1-minimum