class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            count=0
            for j in nums:
                if j>=i:
                    count+=1
                if count>i:
                    break
            if count==i:
                return i
        return -1