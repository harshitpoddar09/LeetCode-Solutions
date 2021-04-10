class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        count=0
        for i in range(2,n+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                count+=1
        ans=1
        for p in range(2,count+1):
            ans*=p
        for q in range(2,n-count+1):
            ans*=q
        return ans%((10**9)+7)