#Submission2 - 44ms
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        while len(bits)>1:
            if bits[0]==1:
                bits.pop(0)
                bits.pop(0)
            else:
                bits.pop(0)
        return len(bits)
        
#Submission1 - 56ms
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        while i<len(bits)-1:
            if bits[i]==1:
                bits.pop(i)
                bits.pop(i)
            else:
                bits.pop(i)
        return len(bits)