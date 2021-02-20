class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        for i in range(1,n+1):
            fact*=i
        fact=str(fact)[::-1]
        count=0
        j=0
        while fact[j]=='0':
            count+=1
            j+=1
        return count