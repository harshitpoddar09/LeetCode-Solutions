class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum=[0]
        n=len(nums)
        for i in nums:
            prefix_sum+=[i+prefix_sum[-1]]
        ans=[]
        for i in range(n):
            ans+=[(i*nums[i]-prefix_sum[i])+(prefix_sum[n]-prefix_sum[i]-((n-i)*nums[i]))]
        return ans