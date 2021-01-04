class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        num=0
        for j in range(len(A)-1,-1,-1):
            num=num+A[j]*(10**(len(A)-1-j))
        num=num+K
        ans=[]
        for i in str(num):
            ans.append(i)
        while len(ans)<len(A):
            ans.insert(0,0)
        return ans