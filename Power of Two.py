class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return 0
        if n==1:
            return 1
        return not(n&(n-1))