class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float('inf')
        w_start=0
        for w_end in range(len(nums)):
            if w_end-w_start==k-1:
                ans=min(ans,nums[w_end]-nums[w_start])
                w_start+=1
        return ans