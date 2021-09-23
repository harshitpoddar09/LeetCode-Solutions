class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        if len(nums)==2:
            return 1
        max_left=[None for i in range(len(nums))]
        min_right=[None for i in range(len(nums))]
        cur_max=nums[0]
        for i in range(len(nums)):
            cur_max=max(cur_max,nums[i])
            max_left[i]=cur_max
        cur_min=nums[-1]
        for i in range(len(nums)-1,-1,-1):
            cur_min=min(cur_min,nums[i])
            min_right[i]=cur_min
        for i in range(1,len(nums)):
            if max_left[i-1]<=min_right[i]:
                return i