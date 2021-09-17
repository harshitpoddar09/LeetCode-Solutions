class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        a=[i for i in range(1,n+1)]
        x=0
        while len(a)!=1:
            b=((x+k)%len(a))-1
            a.pop(b)
            x=b
            if b==-1:
                x=0
        return a[0]