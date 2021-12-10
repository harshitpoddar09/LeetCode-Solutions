class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor=x^y
        b=bin(xor)
        ans=0
        for i in b:
            if i=='1':
                ans+=1
        return ans