class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans1=len(nums)
        ans2=len(nums)
        if target in nums[start::-1]:
            ans1=nums[start::-1].index(target)
        if target in nums[start:]:
            ans2=nums[start:].index(target)
        return min(ans1,ans2)