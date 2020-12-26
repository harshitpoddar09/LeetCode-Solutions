class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        for i in range(len(nums)-1):
            if nums[i]==0 and nums[i+1]!=0:
                nums.pop(i)
                nums.append(int(0))
        """
        i=0
        count=nums.count(0)
        while i<=len(nums)-count-1:
            if nums[i]==0:
                nums.pop(i)
                nums.append(int(0))
            else:
                i+=1