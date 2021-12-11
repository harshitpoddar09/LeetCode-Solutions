#Submission 3 - 68ms
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2==1 and nums[mid]==nums[mid-1]):
                l=mid+1
            else:
                r=mid
        return nums[l]

#Submission 2 - 60ms
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0
        while i+1<len(nums):
            if nums[i]!=nums[i+1]:
                return nums[i]
            i+=2
        return nums[-1]

#Submission 1 - 4988ms
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==1:
                return i