class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        ans=0
        cur_sum=0
        for i in nums:
            cur_sum+=i
            cur_sum=max(0,cur_sum)
            ans=max(ans,cur_sum)
        return ans