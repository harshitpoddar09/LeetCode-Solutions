class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        ans=0
        w_str=''
        for w_end in range(len(s)):
            w_str+=s[w_end]
            if w_end>=2:
                ans+=len(set(w_str))==3
                w_str=w_str[1:]
        return ans