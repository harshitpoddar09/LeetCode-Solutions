class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        if n==0:
            return a
        elif n==1:
            return b
        elif n==2:
            return c
        for i in range(n-2):
            temp=a+b+c
            a=b
            b=c
            c=temp
        return c