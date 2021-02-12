#Method 1
"""
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
"""

#Method 2, faster and takes less space
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1]<target:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i]>=target:
                    return i 
