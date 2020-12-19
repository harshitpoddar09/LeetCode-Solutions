class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add=bin(int(a,2)+int(b,2))
        ans=[]
        for i in add:
            ans.append(i)
        ans.pop(0)
        ans.pop(0)
        binary_sum=''.join(ans)
        return binary_sum