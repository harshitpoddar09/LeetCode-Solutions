#Submission2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
 
#Submission1
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>1:
                return i
