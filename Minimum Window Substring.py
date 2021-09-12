from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window=''
        w_start=0
        ans=2*s
        d=Counter(t)
        for w_end in range(len(s)):
            window+=s[w_end]
            if s[w_end] in d:
                d[s[w_end]]-=1
            while max(d.values())==0:
                if len(window)<len(ans):
                    ans=window
                window=window[1:]
                if s[w_start] in d:
                    d[s[w_start]]+=1
                w_start+=1
        if ans==2*s:
            return ''
        return ans