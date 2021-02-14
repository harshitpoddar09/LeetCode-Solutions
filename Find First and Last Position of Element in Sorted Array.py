class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                ans=[i,i+nums.count(target)-1]
                break
        return ans