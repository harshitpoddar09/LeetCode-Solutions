class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                length.append(count)
                count=0
        length.append(count)
        if len(length)==0:
            return '0'
        else:
            return max(length)