class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        p=list(pattern)
        if len(s)!=len(p):
            return False
        ds={}
        dp={}
        j,k=0,0
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]]=str(j)
                j+=1
            s[i]=ds[s[i]]    
            if p[i] not in dp:
                dp[p[i]]=str(k)
                k+=1
            p[i]=dp[p[i]]
        return p==s