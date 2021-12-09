class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                c+=1
                idx=i
        if c==0:
            return True
        if c==1:
            if idx==0 or idx==len(nums)-2:
                return True
            if nums[idx]<nums[idx+2] or nums[idx+1]>nums[idx-1]:
                return True
        return False