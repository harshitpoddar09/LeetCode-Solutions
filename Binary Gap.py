class Solution:
    def binaryGap(self, n: int) -> int:
        n=bin(n).replace('0b','')
        index=[i for i in range(len(n)) if n[i]=='1']
        if len(index)<=1:
            return 0
        ans=0
        for j in range(len(index)-1):
            ans=max(ans,index[j+1]-index[j])
        return ans