#Submission 2 - 48ms
class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        n=bin(n)[2:]
        n='0'*(32-len(n))+n
        return int(n[::-1],2)
        
#Submission 1 - 40ms
class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        n=bin(n)[2:]
        n='0'*(32-len(n))+n
        for i in range(len(n)):
            ans+=int(n[i])*(2**i)
        return ans