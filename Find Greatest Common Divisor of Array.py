class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        def gcd(a,b):
            ans=1
            for i in range(a+1,1,-1):
                if b%i==0 and a%i==0:
                    return i
            return 1
        return gcd(nums[0],nums[-1])