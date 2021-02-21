#Submission 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sorted(set(nums))!=sorted(nums)

#Submission 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        nums.sort()
        a=sorted(a)
        return a!=nums
