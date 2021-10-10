class Solution:
    def convertToTitle(self, n: int) -> str:
        ans=''
        while n:
            n=n-1
            rem=n%26
            ans=chr(65+rem)+ans
            n=n//26
        return ans