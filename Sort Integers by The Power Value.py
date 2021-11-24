class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power=[]
        for i in range(lo,hi+1):
            n=i
            count=0
            while n!=1:
                if n%2==0:
                    n=n//2
                else:
                    n=3*n+1
                count+=1
            power.append([count,i])
        return sorted(power)[k-1][1] 