class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num)[2:]
        b='1'*len(a)
        c=int(b,2)
        ans=num^c
        return ans