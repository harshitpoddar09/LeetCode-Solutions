class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=1
        curmin=1
        ans=nums[0]
        for i in nums:
            a=[i,curmax*i,curmin*i]
            curmax=max(a)
            curmin=min(a)
            ans=max(ans,curmax)
        return ans