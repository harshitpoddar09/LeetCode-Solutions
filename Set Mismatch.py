class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            if nums.count(i)==2:
                ans.append(i)
                break
        for j in range(len(nums)):
            if j+1 not in nums:
                ans.append(j+1)
                return ans