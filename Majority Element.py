class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=set(nums)
        for i in a:
            if nums.count(i)>len(nums)//2:
                return i