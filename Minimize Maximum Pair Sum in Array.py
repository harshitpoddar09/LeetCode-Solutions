class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        ans=0
        cur=0
        while l<r:
            cur=nums[l]+nums[r]
            ans=max(ans,cur)
            l+=1
            r-=1
        return ans