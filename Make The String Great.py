class Solution:
    def makeGood(self, s: str) -> str:
        i=0
        s=list(s)
        while i+2<=len(s):
            if abs(ord(s[i])-ord(s[i+1]))==32:
                s.pop(i)
                s.pop(i)
                if i>0:
                    i-=1
            else:
                i+=1
        return ''.join(s)