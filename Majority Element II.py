class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in set(nums):
            if nums.count(i)>len(nums)//3:
                ans.append(i)
        return ans
