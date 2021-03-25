class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(sum(nums[0:i+1]))
        return ans