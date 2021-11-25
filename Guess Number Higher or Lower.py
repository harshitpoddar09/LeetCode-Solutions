# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binary(low,high):
            mid=(high+low)//2
            x=guess(mid)
            if x==0:
                return mid
            elif x==1:
                return binary(mid+1,high)
            else:
                return binary(low,mid-1)
        return binary(1,n)