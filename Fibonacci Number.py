class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        a=0
        b=1
        i=0
        f=0
        while i<n-1:
            f=a+b
            c=f
            a=b
            b=c
            i+=1
        return f