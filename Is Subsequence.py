class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if s and i==s[0]:
                s=s.replace(s[0],'',1)
        return len(s)==0