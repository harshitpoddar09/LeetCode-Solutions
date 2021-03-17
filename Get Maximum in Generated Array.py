class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[0,1]
        if n==0:
            return 0
        for i in range(1,n//2):
            nums.insert(2*i,nums[i])
            nums.insert(2*i+1,nums[i]+nums[i+1])
        nums.insert(2*(n//2),nums[n//2])
        if n%2!=0:
            nums.insert((2*(n//2))+1,nums[n//2]+nums[n//2 + 1])
        return max(nums)