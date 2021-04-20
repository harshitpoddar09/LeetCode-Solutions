class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=''
        ans+=s[0+k-1::-1]
        ans+=s[0+k:0+(2*k)]
        for i in range(2*k,len(s),2*k):
            ans+=s[i+k-1:i-1:-1]
            ans+=s[i+k:i+(2*k)]
        return ans