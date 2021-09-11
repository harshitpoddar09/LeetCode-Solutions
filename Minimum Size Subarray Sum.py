class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=len(nums)+1
        w_sum=0
        w_start=0
        for w_end in range(len(nums)):
            w_sum+=nums[w_end]
            while w_sum>=target:
                ans=min(ans,w_end-w_start+1)
                w_sum-=nums[w_start]
                w_start+=1
        if ans==len(nums)+1:
            return 0
        return ans