class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=sum(nums[:k])
        cur_sum=ans
        for i in range(k,len(nums)):
            cur_sum+=nums[i]-nums[i-k]
            ans=max(ans,cur_sum)
        return ans/k