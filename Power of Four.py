class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return 0
        if n==1:
            return 1
        while n>1:
            if n%4!=0:
                return 0
            else:
                n=n/4
        return 1