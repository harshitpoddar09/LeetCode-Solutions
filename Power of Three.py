class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return 0
        if n==1:
            return 1
        while n>1:
            if n%3!=0:
                return 0
            else:
                n=n/3
        return 1