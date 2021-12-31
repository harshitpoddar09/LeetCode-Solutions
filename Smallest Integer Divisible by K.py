#Submission 2 - 1972ms
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%10 in {2,4,5,6,8,0}:
            return -1
        rem=0
        num=0
        for ans in range(1,k+1):
            num=(num*10+1)
            rem=num%k
            if rem==0:
                return ans
        return -1

#Submission 1 - 6752ms
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem=0
        num=0
        for ans in range(1,k+1):
            num=(num*10+1)
            rem=num%k
            if rem==0:
                return ans
        return -1