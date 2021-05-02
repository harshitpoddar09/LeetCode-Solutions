class Solution:
    def thousandSeparator(self, n: int) -> str:
        n=str(n)[::-1]
        ans=''
        i=0
        while i+3<len(n):
            ans+=n[i:i+3]+'.'
            i+=3
        ans+=n[i:i+3]
        return ans[::-1]