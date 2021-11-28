#Submission 2 - 2026ms 23.6mb
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        a=sum(rolls)
        m=len(rolls)
        b=mean*(n+m)-a #mean=(a+b)/(n+m)
        approx=b/n
        if approx>6 or approx<1:
            return []
        fixed=b//n
        extra=b%n
        ans=[fixed]*n
        for i in range(extra):
            ans[i]+=1
        return ans

#Submission 1 - 3314ms 24.2mb
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        a=sum(rolls)
        m=len(rolls)
        b=mean*(n+m)-a #mean=(a+b)/(n+m)
        approx=b/n
        if approx>6 or approx<1:
            return []
        if b/n==b//n:
            return [b//n]*n
        ans=[]
        while n:
            dice=round(b/n)
            ans.append(dice)
            b-=dice
            n-=1
        if b!=0:
            return []
        return ans