class Solution:
    def titleToNumber(self, s: str) -> int:
        ans=0
        s=s[::-1]
        for i in range(len(s)):
            ans+=(26**i)*(ord(s[i])-64)
        return ans