class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set(nums)
        nums.sort()
        a=sorted(a)
        return a!=nums