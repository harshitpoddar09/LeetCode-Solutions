class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2==0:
            ans=('a'*(n-1))+'b'
        else:
            ans='a'*n
        return ans