class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        cur_min=nums[0]
        for i in nums:
            if i>cur_min:
                ans=max(ans,i-cur_min)
            cur_min=min(i,cur_min)
        return ans