class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return '1'
        if nums[len(nums)-1]<=0:
            return '1'
        for i in range(1,nums[len(nums)-1]+2):
            if i not in nums:
                return i