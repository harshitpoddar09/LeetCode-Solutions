Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        ans.append(i)
                        ans.append(j)
        ans.pop(3)
        ans.pop(2)
        return ans