class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return 0
        for i in t:
            if s.count(i)!=t.count(i):
                return 0
        return 1
