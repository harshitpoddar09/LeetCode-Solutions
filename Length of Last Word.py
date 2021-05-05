class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s[-1]==" " and len(s)>1:
            s=s[:len(s)-1]
        if s[-1]==" ":
            s=s[0]
        words=list(s.split(" "))
        return len(words[-1])