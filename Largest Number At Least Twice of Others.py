class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest=max(nums)
        ans=nums.index(largest)
        nums.sort()
        if len(nums)>1:
            if nums[len(nums)-2]>0:
                factor=largest//nums[len(nums)-2]
                if factor<2:
                    ans=-1
        return ans
