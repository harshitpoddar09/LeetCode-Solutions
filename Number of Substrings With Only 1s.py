class Solution:
    def numSub(self, s: str) -> int:
        ans=0
        cur=0
        for w_end in range(len(s)):
            if s[w_end]=='0':
                if cur:
                    ans+=(cur*(cur+1))//2
                    cur=0
            else:
                cur+=1
        if s[-1]=='1':
            ans+=(cur*(cur+1))//2
        return ans%(10**9+7)