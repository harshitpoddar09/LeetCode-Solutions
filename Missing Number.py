#Submission 2 - 132 ms
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) not in nums:
            return len(nums)
        for i in range(len(nums)+1):
            if i!=nums[i]:
                return i

#Submission 1 - 2420ms
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
