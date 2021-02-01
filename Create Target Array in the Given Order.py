class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        i=0
        target=[]
        while i<len(nums):
            target.insert(index[i],nums[i])
            i+=1
        return target