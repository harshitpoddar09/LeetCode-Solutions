class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[len(nums)-1]<target:
                ans=len(nums)
                break
            elif nums[i]>=target:
                ans=i
                break 
        return ans