class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a=bin(n).replace("0b", "")
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                return False
        return True