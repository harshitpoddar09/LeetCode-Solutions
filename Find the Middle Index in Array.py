class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        ls=0
        rs=total-nums[0]
        for i in range(len(nums)-1):
            if ls==rs:
                return i
            ls+=nums[i]
            rs-=nums[i+1]
        if total-nums[-1]==0:
            return len(nums)-1
        return -1