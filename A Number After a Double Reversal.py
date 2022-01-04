class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        s=str(num)
        a=int(s[::-1])
        b=str(a)
        c=int(b[::-1])
        return num==c