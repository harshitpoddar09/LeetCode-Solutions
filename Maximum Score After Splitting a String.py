class Solution:
    def maxScore(self, s: str) -> int:
        ans=0
        for i in range(1,len(s)):
            if s[:i].count('0')+s[i:len(s)].count('1')>ans:
                ans=s[:i].count('0')+s[i:len(s)].count('1')
        return ans